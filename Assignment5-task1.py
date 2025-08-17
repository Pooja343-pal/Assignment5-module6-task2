# Step 1: Create a dictionary of students and their marks
students = {
    "Alice": 85,
    "Pooja": 92,
    "Rahul": 78,
    "Sneha": 88,
    "Kiran": 95
}

# Step 2: Ask user to input a student's name
name = input("Enter the student's name: ")

# Step 3 & 4: Retrieve and display marks (or error message)
if name in students:
    print(f"{name}'s marks = {students[name]}")
else:
    print(f"Student not found.")