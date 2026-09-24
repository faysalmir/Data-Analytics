#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
print(sys.version)
print(sys.executable)


# In[ ]:


conda create -n psx python=3.13 -y #get value from sys.version for python
conda activate psx
pip install psxdata pandas openpyxl jupyter


# In[12]:


#%pip install  psxdata pandas openpyxl # if you donot want to install in an enviroment but whrere python in install


# In[8]:


import os
os.chdir(r"C:\Users\ZA Technologies\Downloads")


# In[2]:


import psxdata

# One company
df = psxdata.stocks(
    "OGDC",
    start="2021-09-23",
    end="2026-09-23"
)


# In[3]:


print(df)


# In[4]:


df.to_csv("OGDC_5years.csv")


# In[3]:


import sys
print(sys.version)
print(sys.executable)


# In[5]:


pwd()


# In[9]:


print(os.getcwd())


# In[1]:


import psxdata
import pandas as pd

# Stocks you want
tickers = ["OGDC", "PPL", "HBL", "MCB", "UBL", "LUCK", "PSO"]

# Get current KSE-100 constituents automatically
#tickers = psxdata.tickers(index="KSE100")

print("Number of stocks:", len(tickers))
print(tickers)

start_date = "2021-09-23"
end_date   = "2026-09-23"

all_data = []

for ticker in tickers:

    try:
        print(f"Downloading {ticker}...")

        df = psxdata.stocks(
            ticker,
            start=start_date,
            end=end_date
        )

        if not df.empty:
            df["symbol"] = ticker
            all_data.append(df)

    except Exception as e:
        print(f"Problem with {ticker}: {e}")

# Combine all stocks
data = pd.concat(all_data, ignore_index=True)

# Arrange columns
data = data[
    ["date", "symbol", "open", "high",
     "low", "close", "volume", "is_anomaly"]
]

# Sort panel
data = data.sort_values(["symbol", "date"])

# Save CSV
data.to_csv(
    "KSE100_daily_5years.csv",
    index=False
)

# Save Excel
data.to_excel(
    "KSE100_daily_5years.xlsx",
    index=False
)

print("\nFinished.")
print("Observations:", len(data))
print("Stocks:", data["symbol"].nunique())

print(data.head())


# In[ ]:




