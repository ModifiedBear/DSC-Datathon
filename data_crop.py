from dask import dataframe as dd
df = dd.read_csv('data.csv')

part = df.partitions[]
