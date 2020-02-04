import pandas as pd
import numpy as np
from plotly.graph_objs import *


# Data obtained from Binance on 2020-02-04
# Read data with 1 day ticks, it will be used to compute indicators
df_1d = pd.read_csv("data/BTCUSDT_1day_ticks.csv")  # you can change here for ETH
# Read data with 1 hour ticks, it will be used to simulate price monitoring
df_1h = pd.read_csv("data/BTCUSDT_1hour_ticks.csv")  # you can change here for ETH

# Compute indicators
df_1d["Close_1_shift"] = df_1d["Close"].shift(1)  # previous day Close value
df_1h["Close_1_shift_1h"] = df_1h["Close_1h"].shift(1)  # previous hour Close value

# In the data table, the current row will be used as present, so only Open value will be known
# other values need to be used from previous row, otherwise we will be cheating in the backtest (it will be overfit!)

df_1d["TR"] = np.abs(df_1d.High - df_1d.Low)
df_1d["TR"] = np.maximum(
    df_1d["TR"],
    np.maximum(
        np.abs(df_1d.Close_1_shift - df_1d.High),
        np.abs(df_1d.Close_1_shift - df_1d.Low),
    ),
)
# The N value from Turtle Algorithm
n_array = np.array(df_1d["TR"].values)
n_array[20] = np.mean(df_1d["TR"][:20])
for i in range(21, df_1d.shape[0]):
    n_array[i] = (19.0 * n_array[i - 1] + df_1d["TR"][i]) / 20.0
df_1d["N"] = n_array

# Compute upper and lower bounds based on Turtle Algorithm
df_1d["upper_bound"] = df_1d["High"].shift(1).rolling(window=20).max()
df_1d["lower_bound"] = df_1d["Low"].shift(1).rolling(window=10).min()

# Join data sets
df = df_1h.merge(df_1d, on="Date", how="left")

# Start the backtest simulation
capital = 1000.0  # initial capital value in USDT
crypto = 0  # the initial amount of crypto
fees = 0.001  # fees as 0.1%
positions = []  # list to keep current positions
success_history = []  # list to keep successful positions
failure_history = []  # list to keep failed positions

print("-" * 50)
print("Initial capital", capital)
print("-" * 50)
# the simulation loop
for i in range(
    21 * 24, df.shape[0]
):  # we start the loop from 21 day, to have N filled properly

    # Check for open position
    # The previous hour Close value is larger than upper bound and we have 0 positions
    if (
        df["Close_1_shift_1h"].iloc[i] > df["upper_bound"].iloc[i]
        and len(positions) == 0
    ):

        # We will use average price from the current ticker
        price = (df["Close_1h"].iloc[i] + df["Open_1h"].iloc[i]) / 2.0
        step = capital * (1.0 - fees)
        crypto += np.round(step / price, 4)
        capital = 0.0  # all capital used
        stop_loss = price - 2.0 * df["N"].iloc[i]  # set stop loss
        positions += [{"time": i, "date": df.Date_1h.iloc[i], "price": price}]

        print(
            "Open position @",
            price,
            "buy",
            crypto,
            "date",
            df.Date_1h.iloc[i],
            "Stop loss @",
            stop_loss,
        )

    # Check to close position
    elif len(positions) > 0 and (
        df["Close_1_shift_1h"].iloc[i]
        < df["lower_bound"].iloc[i]  # we are lower than lower bound
        or df["Close_1_shift_1h"].iloc[i] < stop_loss  # we are lower than stop loss
        or i
        == df.shape[0] - 1  # the end of simulation and we want to close all positions
    ):

        price = (df["Close_1h"].iloc[i] + df["Open_1h"].iloc[i]) / 2.0
        capital = crypto * price * (1 - fees)
        stop_loss, crypto = 0.0, 0.0
        print("Close position @", price, "capital", capital, "date", df.Date_1h.iloc[i])
        if positions[-1]["price"] < price:
            for p in positions:
                success_history += [
                    {
                        "date": [p["date"], df.Date_1h.iloc[i]],
                        "price": [p["price"], price],
                    }
                ]
        else:
            for p in positions:
                failure_history += [
                    {
                        "date": [p["date"], df.Date_1h.iloc[i]],
                        "price": [p["price"], price],
                    }
                ]
        positions = []

success_rate = 0
if len(success_history) + len(failure_history) > 0:
    success_rate = len(success_history) / (len(failure_history) + len(success_history))

print("-" * 50)
print("Success rate", success_rate)
print("Capital at the end", np.round(capital, 2))
print("-" * 50)
print("Summary of % change in positions")
price_changes = []
for h in [failure_history, success_history]:
    for position in h:
        percent_change = np.round(
            (position["price"][1] - position["price"][0])
            / position["price"][0]
            * 100.0,
            2,
        )
        print("Percent change in position", percent_change)

# plot them
trace0 = Candlestick(x=df.Date, open=df.Open, high=df.High, low=df.Low, close=df.Close)
fig = Figure()
fig.add_trace(trace0)

for f in failure_history:
    trace = Scatter(
        x=f["date"],
        y=f["price"],
        mode="markers+lines",
        marker_color="rgba(2, 2, 3, .9)",
    )
    fig.add_trace(trace)

for f in success_history:
    trace = Scatter(
        x=f["date"],
        y=f["price"],
        mode="markers+lines",
        marker_color="rgba(2, 255, 3, .9)",
    )
    fig.add_trace(trace)

fig.show()
