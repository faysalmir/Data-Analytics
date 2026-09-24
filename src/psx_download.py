import pandas as pd
import psxdata


def download_stocks(tickers, start_date, end_date):
    """
    Download daily historical data for multiple PSX stocks.

    Parameters
    ----------
    tickers : list of str
        PSX ticker symbols, e.g. ["OGDC", "PPL", "HBL"].

    start_date : str
        Starting date in YYYY-MM-DD format.

    end_date : str
        Ending date in YYYY-MM-DD format.

    Returns
    -------
    pandas.DataFrame
        Combined panel dataset containing all successfully
        downloaded stocks.
    """

    all_data = []

    for ticker in tickers:

        try:
            print(f"Downloading {ticker}...")

            df = psxdata.stocks(
                ticker,
                start=start_date,
                end=end_date
            )

            if df.empty:
                print(f"No data found for {ticker}")
                continue

            df["symbol"] = ticker

            all_data.append(df)

        except Exception as error:
            print(f"Failed to download {ticker}: {error}")

    if not all_data:
        raise ValueError("No stock data were downloaded.")

    data = pd.concat(
        all_data,
        ignore_index=True
    )

    data = data.sort_values(
        ["symbol", "date"]
    ).reset_index(drop=True)

    return data
