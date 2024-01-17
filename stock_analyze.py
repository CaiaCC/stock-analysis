from datetime import datetime
from dateutil.relativedelta import relativedelta
import pandas as pd
import yfinance as yf

# the stocks tickers for analysis
tickers = ["MSFT", "GOOGL", "AAPL"]

# Get the start and end dates of 3 month time frame
end_date = datetime.now()
start_date = datetime.now() + relativedelta(months=-3)

