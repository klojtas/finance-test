import yfinance as yf

orsted = yf.Ticker("ORSTED.CO")

print("=== Orsted information ===")
print(orsted.income_stmt["2024-12-31"]["EBITDA"])
