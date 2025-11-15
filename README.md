# finance-test

Test repository to verify the finance data extraction

## Prerequirements

### Install uv

powershell

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

pip

```bash
pip install uv
```

check uv

```bash
uv --version
```

### pre-commit hooks

Installation

```bash
uv pip install pre-commit
uv run pre-commit install
```

Test

```bash
uv run pre-commit run --all-files
```

## Python prepare

### Create virtual environment

```bash
uv venv
```

### Activate python virtual envi

```powershell
.venv\Scripts\activate
```

## Examples

### example-0.py

Retrieves and displays basic ticker information for ORSTED.CO stock
using `yfinance.Ticker.info`.

### example-1.py

Extracts comprehensive financial data for ORSTED.CO including major
holders, institutional holders, mutual fund holders, sustainability data,
financial statements, income statements, recommendations, and sentiment.

### example-2.py

Accesses specific financial metrics from the income statement (e.g.,
EBITDA for a specific date) using nested dictionary access.

### example-3.py

Converts ticker information into a pandas Series for easier access and
manipulation. Demonstrates printing all available keys and accessing
specific metrics like `currentPrice`.

### example-4.py

Collects and compares financial ratios across multiple tickers (WMT, MO,
NVDA, CRM) and returns a pandas DataFrame with sectors, industries, and
financial ratios.

### example-5.py

Fetches historical price data for ORSTED.CO over a custom date range
(2023-01-01 to 2025-11-15) and displays the resulting DataFrame.

### example-6.py

Plots normalized closing prices as a percentage change from the initial
price for multiple tickers (AAPL, SMR, MSTR) over the last year.

### example-7.py

Creates a histogram visualization of daily returns (percentage changes)
for ORSTED.CO stock over the last year with 200 bins to show return
distribution.
