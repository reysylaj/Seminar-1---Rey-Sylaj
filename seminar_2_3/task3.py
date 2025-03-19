import pandas as pd

# Load the dataset
file_path = "Rrogat.csv"  # Ensure the file is in the same folder as this script
df = pd.read_csv(file_path)

# Get the number of rows and columns
num_rows, num_columns = df.shape

# Print the result
print(f"Total rows: {num_rows}")
print(f"Total columns: {num_columns}")
