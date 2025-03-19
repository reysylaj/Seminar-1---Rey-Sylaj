import pandas as pd

# Load the dataset
file_path = "Rrogat.csv"  # Ensure the file is in the same folder as this script
df = pd.read_csv(file_path)

# Find the total income including benefits for JOSEPH DRISCOLL
total_income_joseph = df[df["EmerPunonjesi"] == "JOSEPH DRISCOLL"]["PerfitimeTotale"].values

# Print the result
if len(total_income_joseph) > 0:
    print(f"Total income including benefits for JOSEPH DRISCOLL: {total_income_joseph[0]:.2f}")
else:
    print("JOSEPH DRISCOLL not found in the dataset.")
