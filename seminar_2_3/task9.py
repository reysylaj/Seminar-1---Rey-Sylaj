import pandas as pd

# Load the dataset
file_path = "Rrogat.csv"  # Ensure the file is in the same folder as this script
df = pd.read_csv(file_path)

# Find the employee with the lowest value in the 'PerfitimeTotale' column
lowest_paid_employee = df.loc[df["PerfitimeTotale"].idxmin(), ["EmerPunonjesi", "PerfitimeTotale"]]

# Print the result
print(f"Punonjesi me pak i paguar duke perfshire perfitimet eshte: {lowest_paid_employee['EmerPunonjesi']}")
