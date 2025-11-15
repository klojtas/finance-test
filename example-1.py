import yfinance as yf

orsted = yf.Ticker("ORSTED.CO")

print("=== Orsted information ===")
print(orsted.info)

print("=== Orsted major holders ===")
print(orsted.major_holders)

print("=== Orsted institutional holders ===")
print(orsted.institutional_holders)

print("=== Orsted mutual fund holders ===")
print(orsted.mutualfund_holders)

print("=== Orsted sustainability ===")
print(orsted.sustainability)

print("=== Orsted financials ===")
print(orsted.financials)

print("=== Orsted balance sheet ===")
print(orsted.balance_sheet)

print("=== Orsted cashflow ===")
print(orsted.cashflow)

print("=== Orsted quarterly earnings ===")
print(orsted.quarterly_earnings)

print("=== Orsted income statement ===")
print(orsted.income_stmt)

print("=== Orsted quarterly income statement ===")
print(orsted.quarterly_income_stmt)

print("=== Orsted recommendations ===")
print(orsted.recommendations)

print("=== Orsted sentiment ===")
print(orsted.sentiment)
