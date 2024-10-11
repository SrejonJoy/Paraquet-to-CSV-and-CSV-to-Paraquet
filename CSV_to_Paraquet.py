import pandas as pd
import pyarrow.parquet as pq

# Specify the paths to your CSV files
csv_files = [
    "output0.csv",
    "output1.csv",
    "output2.csv"
]

dfs = []
for file in csv_files:
    df = pd.read_csv(file)
    dfs.append(df)

# Concatenate all DataFrames horizontally
merged_df = pd.concat(dfs, axis=0, ignore_index=True)

# Display the merged DataFrame
print(merged_df.head())

# Write the merged DataFrame to a Parquet file
merged_df.to_parquet("merged_output.parquet")

# Optionally, you can also print the schema
print("\nSchema:")
print(merged_df.info())

# When you're done, you can close the pandas session
del merged_df
