import pyarrow.parquet as pq
import pandas as pd

# Specify the path to your Parquet file
parquet_file_path = "train-00000-of-00001-258f7b77b36023df.parquet"

# Read the Parquet file
table = pq.read_table(parquet_file_path)

# Convert to pandas DataFrame
df = table.to_pandas()

# Display the first few rows
print(df.head())

# Optionally, you can also print the schema
print(df.info())

# If you want to save the results to a CSV file
df.to_csv("output0.csv", index=False)

# When you're done, you can close the pandas session
del df
