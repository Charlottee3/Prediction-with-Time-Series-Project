import pandas as pd

def read_data():
    df = pd.read_csv('data/raw_data_WWTP.csv', index_col='date', parse_dates=['date'])
    return df