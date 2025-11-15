import pandas as pd

import yfinance as yf


def collect_ratios(tickers: list, ratios: list):
    rows = []
    for ticker in tickers:
        info = yf.Ticker(ticker).info
        row = [ticker] + [info.get(ratio, None) for ratio in ratios]
        rows.append(row)
    return pd.DataFrame(rows, columns=["Ticker"] + ratios)


print(
    collect_ratios(
        ["WMT", "MO", "NVDA", "CRM"],
        ["sector", "industry", "currentRatio", "quickRatio"],
    )
)
