import pandas as pd

# Load the dataset
file_path = "Rrogat.csv"  # Ensure the file is in the same folder as this script
df = pd.read_csv(file_path)

# Find the highest value in the 'Overtime' column
max_overtime = df["Overtime"].max()

# Print the result
print(f"Highest Overtime value: {max_overtime:.2f}")
