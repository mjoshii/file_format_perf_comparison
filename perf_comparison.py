import pandas as pd
import polars as pl
import time

pd_csv_start_time = time.time()
df_pandas = pd.read_csv('all_candidates.csv')
pd_csv_read_time = time.time() - pd_csv_start_time
print(df_pandas.head())

pl_csv_start_time = time.time()
df_polars = pl.read_csv('all_candidates.csv')
pl_csv_read_time = time.time() - pl_csv_start_time
print(df_polars.head())

pd_parquet_start_time = time.time()
df_pandas_par = pd.read_parquet('all_candidates.parquet')
pd_parquet_read_time = time.time() - pd_parquet_start_time
print(df_pandas_par.head())

pl_parquet_start_time = time.time() 
df_polars_par = pl.read_parquet('all_candidates.parquet')
pl_parquet_read_time = time.time() - pl_parquet_start_time
print(df_polars_par.head())

# Add JSON reading for Pandas
pd_json_start_time = time.time()
df_pandas_json = pd.read_json('all_candidates.json')
pd_json_read_time = time.time() - pd_json_start_time
print(df_pandas_json.head())

# Add JSON reading for Polars
pl_json_start_time = time.time()
df_polars_json = pl.read_json('all_candidates.json')
pl_json_read_time = time.time() - pl_json_start_time
print(df_polars_json.head())

print('*' * 75)
print(f"CSV read time using pandas: {pd_csv_read_time}")
print(f"CSV read time using polars: {pl_csv_read_time}")
print(f"Parquet read time using pandas: {pd_parquet_read_time}")
print(f"Parquet read time using polars: {pl_parquet_read_time}")
print(f"JSON read time using pandas: {pd_json_read_time}")
print(f"JSON read time using polars: {pl_json_read_time}")