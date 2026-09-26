# Data Analytics

A Python-based repository for financial data collection, data analytics, econometrics, and machine-learning research.

The current PSX module provides reusable code for downloading daily historical stock data from the Pakistan Stock Exchange (PSX).

## Project Structure

```text
Data-Analytics/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── src/
│   ├── __init__.py
│   └── psx_download.py
│
├── notebooks/
│   └── psx_analysis.ipynb
│
├── data/
│   ├── raw/
│   └── processed/
│
└── results/
```

### Directory Purpose

* `src/` — reusable Python functions and modules.
* `notebooks/` — Jupyter notebooks for analysis and experimentation.
* `data/raw/` — original downloaded datasets.
* `data/processed/` — cleaned or transformed datasets.
* `results/` — model outputs, tables, figures, and other research results.

## 1. Clone the Repository

Install Git and open Command Prompt, PowerShell, Git Bash, or Anaconda Prompt.

Move to the directory where you want to store the project:

```bash
cd D:\Research
```

Clone the repository:

```bash
git clone https://github.com/faysalmir/Data-Analytics.git
```

Move into the project directory:

```bash
cd Data-Analytics
```

## 2. Install Required Python Packages

Install the dependencies using:

```bash
pip install -r requirements.txt
```

The main packages include:

```text
pandas
psxdata
openpyxl
jupyter
numpy
matplotlib
```

## 3. Start Jupyter Notebook

Start Jupyter from the **root directory of the project**:

```bash
jupyter notebook
```

Then open:

```text
notebooks/psx_analysis.ipynb
```

## 4. Configure the Project Path

At the beginning of the notebook, define the project root:

```python
from pathlib import Path
import sys

PROJECT_ROOT = Path.cwd().parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

print("Project root:", PROJECT_ROOT)
```

This allows the notebook to access reusable Python modules stored in `src/`.

## 5. Import the PSX Download Function

```python
from src.psx_download import download_stocks
```

## 6. Select Stocks and Time Period

For example:

```python
tickers = [
    "OGDC",
    "PPL",
    "HBL",
    "MCB",
    "UBL",
    "LUCK",
    "PSO"
]

start_date = "2021-09-23"
end_date = "2026-09-23"
```

## 7. Download PSX Data

Run:

```python
data = download_stocks(
    tickers=tickers,
    start_date=start_date,
    end_date=end_date
)
```

Inspect the downloaded data:

```python
data.head()
```

Check the number of observations and stocks:

```python
print("Observations:", len(data))
print("Stocks:", data["symbol"].nunique())
```

## 8. Create Data and Results Directories

The following code automatically creates the required directories if they do not already exist:

```python
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"
PROCESSED_DATA_DIR = PROJECT_ROOT / "data" / "processed"
RESULTS_DIR = PROJECT_ROOT / "results"

RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)
PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)
RESULTS_DIR.mkdir(parents=True, exist_ok=True)
```

## 9. Save the Downloaded Data

Save the raw PSX data as a CSV file:

```python
file_path = RAW_DATA_DIR / "psx_daily_2021_2026.csv"

data.to_csv(
    file_path,
    index=False
)

print("Saved successfully:")
print(file_path)
```

Verify that the file exists:

```python
print(file_path.exists())
```

If successful, Python should return:

```text
True
```

## Typical Workflow

```text
GitHub Repository
       │
       ↓
Clone repository
       │
       ↓
Install requirements
       │
       ↓
Open Jupyter Notebook
       │
       ↓
Select PSX stocks and dates
       │
       ↓
src/psx_download.py
       │
       ↓
Download stock data
       │
       ↓
data/raw/
       │
       ↓
Cleaning and transformation
       │
       ↓
data/processed/
       │
       ↓
Econometric / ML analysis
       │
       ↓
results/
```

## Updating the Repository

After modifying code or notebooks locally:

```bash
git add .
git commit -m "Update PSX analysis"
git push
```

To obtain the latest changes from GitHub:

```bash
git pull
```

## Reproducibility

Reusable functions should be placed in `src/`, while research analysis and experimentation should remain in `notebooks/`.

Raw downloaded data should remain separate from processed datasets. This structure helps keep financial and econometric research projects reproducible and easier to maintain.
