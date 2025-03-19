import pandas as pd

# Load the dataset
file_path = "Rrogat.csv"  # Ensure the file is in the same folder as this script
df = pd.read_csv(file_path)

# Find the 5 most frequent professions and their frequency
top_5_professions = df["Profesioni"].value_counts().head(5)

# Print the result
print("5 profesionet me te shpeshta jane dhe shpeshtesia per secilen eshte:")
for profession, count in top_5_professions.items():
    print(f"{profession}: {count}")
