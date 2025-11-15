import yfinance as yf

hd_orsted_since_2023 = yf.Ticker("ORSTED.CO").history(
    start="2023-01-01", end="2025-11-15"
)

print(hd_orsted_since_2023)
