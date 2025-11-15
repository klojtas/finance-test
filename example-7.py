import matplotlib.pyplot as plt
import yfinance as yf

history_orsted = yf.Ticker("ORSTED.CO").history(period="1y")
returns_orsted = history_orsted["Close"].pct_change().dropna()
returns_orsted.hist(bins=200, figsize=(20, 15))
plt.title("ORSTED.CO Daily Returns Histogram - Last 1 Year")
plt.show()
