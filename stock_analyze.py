import yfinance as yf
import pandas as pd

msft = yf.Ticker("MSFT")

# get all stock info
info = msft.info
# print(info)

# get historical market data
hist = msft.history(period="1mo")
print(hist)
