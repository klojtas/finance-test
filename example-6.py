import matplotlib.pyplot as plt
import yfinance as yf


def plot_closing_prices(data):
    close_prices = data["Close"]
    price_change_in_percentage = close_prices / close_prices.iloc[0] * 100
    price_change_in_percentage.plot(figsize=(12, 8), fontsize=12)
    plt.ylabel("Percentage")
    plt.title("Price Chart", fontsize=15)
    plt.show()


hd_nvda_smr_aapl_1yr = yf.Tickers(["AAPL", "SMR", "MSTR"]).history(period="1y")
print("Plotting closing prices for AAPL, SMR, and KO over the last year")
plot_closing_prices(hd_nvda_smr_aapl_1yr)
