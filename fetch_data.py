import yfinance as yf
import pandas as pd
import numpy as np

stocks = ['AAPL', 'NVDA', 'MSFT', 'GOOGL', 'META', 'AMZN', 'TSLA', 'AMD', 'JPM', 'KO']
etfs = ['SPY', 'XLK', 'XLF', 'XLV', 'XLE', 'XLY', 'IWM']
proj_tickers = stocks + etfs

data = yf.download(proj_tickers, start='2020-01-01', end='2025-05-01')['Close']
data = data.dropna()

daily_returns = (data - data.shift(1)) / data.shift(1)
daily_returns = daily_returns.dropna()

print("Shape:", data.shape)
print("\nAnnualized mean returns:")
print(daily_returns.mean() * 252)
print("\nAnnualized Volatility:")
print(daily_returns.std() * np.sqrt(252))

data.to_csv('/Users/ryogagrisnik/Desktop/fin project/prices.csv')
daily_returns.to_csv('/Users/ryogagrisnik/Desktop/fin project/returns.csv')