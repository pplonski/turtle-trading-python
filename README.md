# Turtle Trading in Python

This is a backtest of turtle trading algorithm on cryptocurrency data in python.


### Data

 - The example backtest is running on BTC/USDT pair (the data obtained from Binance on 2020-02-04).
 - You can easily change the backtest to run with ETH/USDT data (also from 2020-02-04).
 - The data is already provided in `data` directory
 - I have used cryptocurrency data because it was easy to obtain. What is more, the automatic live trading with bot will be easy because setting account and obtaining API is also easy (without initial capital constraints).

### Requirements

The backtest was computed on Ubuntu 16.04 and python 3.6

Needed packages:
```
pip install pandas numpy plotly
```

### Run backtest

```
python backtest.py
```

Expected output on BTC/USDT data:
```
--------------------------------------------------
Initial capital 1000.0
--------------------------------------------------
Open position @ 4428.99 buy 0.2256 date 2017-10-02 01:00:00.000 Stop loss @ 3774.7765961811365
Close position @ 6195.535 capital 1396.3149833039997 date 2017-11-11 19:00:00.000
Open position @ 7767.225 buy 0.1796 date 2017-11-16 19:00:00.000 Stop loss @ 6682.535921529168
Close position @ 14825.0 capital 2659.90743 date 2017-12-21 16:00:00.000
Open position @ 11442.66 buy 0.2322 date 2018-02-20 01:00:00.000 Stop loss @ 8992.061097120413
Close position @ 9305.52 capital 2158.581002256 date 2018-03-08 18:00:00.000
Open position @ 8501.95 buy 0.2536 date 2018-04-20 11:00:00.000 Stop loss @ 7331.935674604393
Close position @ 8750.17 capital 2216.824068888 date 2018-05-11 08:00:00.000
Open position @ 7265.495 buy 0.3048 date 2018-07-17 18:00:00.000 Stop loss @ 6608.813973488342
Close position @ 7364.0 capital 2242.3026528 date 2018-08-03 01:00:00.000
Open position @ 7035.0 buy 0.3184 date 2018-08-28 12:00:00.000 Stop loss @ 6354.161460452529
Close position @ 6449.5 capital 2051.4672792 date 2018-09-06 01:00:00.000
Open position @ 7135.17 buy 0.2872 date 2018-10-15 07:00:00.000 Stop loss @ 6624.314411513054
Close position @ 6606.355 capital 1895.4478108439998 date 2018-10-18 21:00:00.000
Open position @ 4142.0 buy 0.4572 date 2018-12-24 01:00:00.000 Stop loss @ 3593.4076083448613
Close position @ 3568.26 capital 1629.777063528 date 2018-12-27 20:00:00.000
Open position @ 3726.975 buy 0.4369 date 2019-02-18 04:00:00 Stop loss @ 3481.6959997550325
Close position @ 7645.145 capital 3336.8236866495 date 2019-06-04 18:00:00
Open position @ 9271.165 buy 0.3596 date 2019-06-16 06:00:00 Stop loss @ 8406.041937099604
Close position @ 9809.855 capital 3524.0962341419995 date 2019-07-02 06:00:00
Open position @ 11294.025000000001 buy 0.3117 date 2019-08-05 01:00:00 Stop loss @ 9870.936939813835
Close position @ 10497.755 capital 3268.8780832664997 date 2019-08-14 09:00:00
Open position @ 9613.705 buy 0.3397 date 2019-10-26 01:00:00 Stop loss @ 8622.679672786018
Close position @ 8790.455 capital 2983.1314459365 date 2019-11-08 14:00:00
Open position @ 7735.29 buy 0.3853 date 2020-01-06 23:00:00 Stop loss @ 7143.767789865975
Close position @ 9127.925 capital 3513.4725129974995 date 2020-02-04 13:00:00
--------------------------------------------------
Success rate 0.5384615384615384
Capital at the end 3513.47
--------------------------------------------------
Summary of % change in positions
Percent change in position -18.68
Percent change in position -8.32
Percent change in position -7.41
Percent change in position -13.85
Percent change in position -7.05
Percent change in position -8.56
Percent change in position 39.89
Percent change in position 90.87
Percent change in position 2.92
Percent change in position 1.36
Percent change in position 105.13
Percent change in position 5.81
Percent change in position 18.0
Created new window in existing browser session.
```

There will be window opened in your browser to show backtest results. Similar to the backtest below:

<p align="center">
<img src="https://raw.githubusercontent.com/pplonski/turtle-trading-python/master/misc/default_backtest.png" width=450 />
</p>

The green lines are showing profitable positions, whereas black lines are for loss positions.

### Advanced Turtle Trading

I'm considering writing a more advanced tutorial about using turtle trading on cryptocurrency data in Python. The tutorial will cover:

 - How to get historical and live data from Binance with their API.
 - How to backtest long and short strategy with Turtle Trading Algorithm.
 - How to create long and short strategy for live trading.
 - How to tune Turtle Trading Algorithm for better performance.

The example of tuned long strategy on BTC/USDT data:

<p align="center">
<img src="https://raw.githubusercontent.com/pplonski/turtle-trading-python/master/misc/advanced_backtest.png" width=450 />
</p>


[Please notify me when it will be ready and get 20% off!](https://forms.gle/3eXGqSGXeotS3h6g9)

#### Cross-selling

You can also check my previously written tutorial: [How to deploy machine learning models with Django](https://deploymachinelearning.com)