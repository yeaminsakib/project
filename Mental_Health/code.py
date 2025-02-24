import pandas as pd

# Load the dataset (Make sure to replace '11111.csv' with the correct file path if needed)
df = pd.read_csv("11111.csv")

# Count the number of males and females
gender_counts = df["Gender"].value_counts()

# Display the counts
print(gender_counts)
