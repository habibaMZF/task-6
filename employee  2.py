import pandas as pd

# Create the DataFrame
students_data = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [20, 22, 19, 21, 20],
    "Grade": ["A", "B", "A", "C", "B"],
    "Marks": [85, 78, 92, 65, 74]
})

# Display the first 3 rows
print("First 3 rows:")
print(students_data.head(3))

# Select and display only Name and Marks columns
print("\nName and Marks columns:")
print(students_data[["Name", "Marks"]])

# Filter students with Grade 'A'
print("\nStudents with Grade A:")
print(students_data[students_data["Grade"] == "A"])