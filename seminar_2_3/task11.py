import pandas as pd

# Load the dataset
file_path = "Rrogat.csv"  # Ensure the file is in the same folder as this script
df = pd.read_csv(file_path)

# Count the number of unique professions
num_unique_professions = df["Profesioni"].nunique()

# Print the result
print(f"The number of unique professions in this dataset is: {num_unique_professions}")
