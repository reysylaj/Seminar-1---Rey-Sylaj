import pandas as pd

# Load the dataset
file_path = "Rrogat.csv"  # Ensure the file is in the same folder as this script
df = pd.read_csv(file_path)

# Find the employee with the highest value in the 'PerfitimeTotale' column
highest_paid_employee = df.loc[df["PerfitimeTotale"].idxmax(), ["EmerPunonjesi", "PerfitimeTotale"]]

# Print the result
print(f"Punonjesi me i paguar duke perfshire perfitimet eshte: {highest_paid_employee['EmerPunonjesi']}")
