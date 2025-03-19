import pandas as pd

# Load the dataset
file_path = "Rrogat.csv"  # Ensure the file is in the same folder as this script
df = pd.read_csv(file_path)

# Filter dataset for the years 2011-2014
df_filtered = df[df["Viti"].between(2011, 2014)]

# Group by year and calculate the average RrogaBaze
average_salary_per_year = df_filtered.groupby("Viti")["RrogaBaze"].mean()

# Print results
for year, avg_salary in average_salary_per_year.items():
    print(f"Mesatarja e RrogaBaze per te gjithe punonjesit te cilet kane punuar ne vitin {year} eshte: {avg_salary:.2f}")
