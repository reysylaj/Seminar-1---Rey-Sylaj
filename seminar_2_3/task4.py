import pandas as pd

# Load the dataset
file_path = "Rrogat.csv"  # Ensure the file is in the same folder as this script
df = pd.read_csv(file_path)

# Calculate the average of the 'RrogaBaze' column
avg_salary = df["RrogaBaze"].mean()

# Print the result
print(f"Average RrogaBaze: {avg_salary:.2f}")
