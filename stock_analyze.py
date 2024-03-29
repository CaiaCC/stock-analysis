from datetime import datetime
import pandas as pd
import plotly.express as px
import yfinance as yf


# the stocks tickers for analysis
tickers = ["MSFT", "GOOGL", "AAPL"]

# Get the start and end dates of 3 month time frame
end_date = datetime.now()
start_date = end_date - pd.DateOffset(months=1)

# get the stock data in the past 3 month
df_list = []
for ticker in tickers:
    data = yf.download(tickers, start=start_date, end=end_date)
    df_list.append(data)

print("list", df_list)

df = pd.concat(df_list, keys=tickers, names=['Ticker', 'Date'])
df = df.reset_index()
df.to_csv('StockData.csv')

# print("df", df.head(20))
