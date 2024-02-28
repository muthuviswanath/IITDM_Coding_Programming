import pandas as pa
import yfinance as yf
from datetime import datetime
import plotly.express as plexp

yf.pdr_override()
start = datetime.now() - pa.DateOffset(months=3)
end = datetime.now()

tickers = ['AAPL', 'MSFT', 'NFLX', 'GOOG', 'IBM']

df_list = []
for ticker in tickers:
    data = yf.download(ticker, start=start, end=end)
    df_list.append(data)

df = pa.concat(df_list, keys=tickers, names=['Ticker', 'Date'])
print(df.head())
print(df.tail())

df = df.reset_index()
print(df.head())
print(df.tail())


img_1 = plexp.line(
    df,
    x= 'Date',
    y= 'Close',
    color= 'Ticker',
    title= 'Stock Prices',
)
img_1.show()

img_2 = plexp.area(df,
                   x = 'Date',
                   y = 'Close',
                   facet_col= 'Ticker',
                   labels= {'Date':'Date', 'Close': 'Close Price', 'Ticker': 'Stock Ticker'},
                   title= 'Stock Price Movements'
                   )
img_2.show()

df['MAverage10'] = df.groupby('Ticker')['Close'].rolling(window=10).mean().reset_index(0, drop=True)
df['MAverage20'] = df.groupby('Ticker')['Close'].rolling(window=20).mean().reset_index(0, drop=True)

for ticker, group in df.groupby('Ticker'):
    print(f"Moving Average for {ticker}")
    print(group[['MAverage10', 'MAverage20']])
    print("\n\n")

for ticker,group in df.groupby('Ticker'):
    img_3 = plexp.line(
        group,
        x= 'Date',
        y= ['Close', 'MAverage10', 'MAverage20'],
        title= f"Stock Price and Moving Averages for {ticker}",
    )
    img_3.show()

df['volatility'] = df.groupby('Ticker')['Close'].pct_change().rolling(window=10).std().reset_index(0, drop=True)
img_4 = plexp.line(
    df,x= 'Date',
    y= 'volatility',
    color= 'Ticker',
    title= 'Volatility of Stocks'
)
img_4.show()

apple = df.loc[df['Ticker'] == 'AAPL',['Date','Close']].rename(columns={'Close':'AAPL'})
microsoft = df.loc[df['Ticker'] == 'MSFT',['Date','Close']].rename(columns={'Close':'MSFT'})
correlation = pa.merge(apple,microsoft,on='Date')
img_5 = plexp.scatter(correlation,
                      x = 'AAPL', y = "MSFT",
                      trendline= 'expanding',
                      title="Correlation between APPLE and MICROSOFT Stocks")
img_5.show()