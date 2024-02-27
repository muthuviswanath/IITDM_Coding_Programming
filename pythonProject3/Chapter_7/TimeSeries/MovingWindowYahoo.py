import pandas as pd
import datetime
import yfinance as yf
yf.pdr_override()
from datetime import datetime,date, time
import matplotlib.pyplot as plt
import pandas_datareader.data as web

start = datetime(2020, 1, 1)
end = datetime(2024, 12, 31)

sec = web.DataReader('005930.KS',start,end,'yahoo')
print(sec)
print(sec.info())

#Find the Rolling Window / Scrolling Window

close = sec['Adj Close']
ma5 = sec['Adj Close'].rolling(window=5).mean()
ma20 = sec['Adj Close'].rolling(window=20).mean()
ma60 = sec['Adj Close'].rolling(window=60).mean()
ma120 = sec['Adj Close'].rolling(window=120).mean()

plt.figure(figsize=(15, 10))
plt.plot(close.index, label='Close', linewidth=5)
plt.plot(ma5.index, ma5, label='MA5', linestyle='--')
plt.plot(ma20.index, ma20, label='MA20', linestyle='-.')
plt.plot(ma60.index, ma60, label='MA60', linestyle=':')
plt.plot(ma120.index, ma120, label='MA120', linestyle='-')

plt.legend()
plt.show()

