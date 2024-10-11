import pyarrow.parquet as pq
import pandas as pd

# Specify the path to your Parquet file
parquet_file_path = "train-00000-of-00002.parquet"

# Read the Parquet file
table = pq.read_table(parquet_file_path)

# Convert to pandas DataFrame
df = table.to_pandas()

# Select columns in the desired order
columns_order = ['input', 'instruction', 'output']
df_reordered = df[columns_order]

# Function to display or save the output
def display_or_save(output, filename=None):
    print(output)
    
    if filename:
        print(f"\nSaving to {filename}...")
        df_reordered.to_csv(filename, index=False)
        print(f"Output saved to {filename}")

# Display only the first 5 rows
display_or_save(df_reordered.head(5).to_string(index=False), "output1.csv")

# Optionally, you can also print the schema
print("\nSchema:")
display_or_save(df_reordered.info(), "schema_info1.txt")

# When you're done, you can close the pandas session
del df, df_reordered
