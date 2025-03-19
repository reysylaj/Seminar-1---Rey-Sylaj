import pandas as pd

# Load the dataset
file_path = "Rrogat.csv"  # Ensure the file is in the same folder as this script
df = pd.read_csv(file_path)

# Find the profession of JOSEPH DRISCOLL
profession_joseph = df[df["EmerPunonjesi"] == "JOSEPH DRISCOLL"]["Profesioni"].values

# Print the result
if len(profession_joseph) > 0:
    print(f"Profession of JOSEPH DRISCOLL: {profession_joseph[0]}")
else:
    print("JOSEPH DRISCOLL not found in the dataset.")
