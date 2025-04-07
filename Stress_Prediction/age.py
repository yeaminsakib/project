import random

# Number of students
num_students = 1026

# Generate random ages between 20 and 24
ages = [random.randint(20, 27) for _ in range(num_students)]

# Save the ages to a file
file_path = "date.txt"  # Change this path if you want to store it elsewhere
with open(file_path, "w") as file:
    for i, age in enumerate(ages, start=1):
        file.write(f"{age}\n")

print(f"Student ages have been saved to '{file_path}'.")
