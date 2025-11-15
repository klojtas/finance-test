import yfinance as yf
import pandas as pd

orsted = yf.Ticker("ORSTED.CO")


print(pd.Series(orsted.info))

info = pd.Series(orsted.info)

print(", ".join(info.keys()))

info.currentPrice
