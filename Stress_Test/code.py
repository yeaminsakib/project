import pandas as pd

# Load your dataset first (replace the file path with your own CSV file path)
data = pd.read_csv(E:\Stress_Test\Expanded_Student_Stress_and_Mobile_Addiction_Data.csv)

# Reset the 'Unnamed: 0' column to a serial number sequence starting from 1
data['Unnamed: 0'] = pd.Series(range(1, len(data) + 1))

# Optional: Save the modified dataset if needed
data.to_csv('modified_data.csv', index=False)

# Display the updated dataframe (you can use this to visualize the changes in your code environment)
import ace_tools as tools; tools.display_dataframe_to_user(name="Updated Student Stress and Mobile Addiction Data", dataframe=data)

# Show the first few rows to confirm the update
print(data.head())
