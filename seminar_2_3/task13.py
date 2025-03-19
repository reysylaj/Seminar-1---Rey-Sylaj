import pandas as pd

# Load the dataset
file_path = "Rrogat.csv"  # Ensure the file is in the same folder as this script
df = pd.read_csv(file_path)

# Filter dataset for the year 2013
df_2013 = df[df["Viti"] == 2013]

# Count the occurrences of each profession
profession_counts = df_2013["Profesioni"].value_counts()

# Get professions that appear only once
unique_professions = profession_counts[profession_counts == 1]

# Print the results
print("Profesionet qe kane vetem 1 perfaqesues ne vitin 2013 jane:")
for profession in unique_professions.index:
    print(profession)
