Task 2: Demonstrate List Slicing 
Problem Statement: Write a Python program that:
1.   Creates a list of numbers from 1 to 10.
2.   Extracts the first five elements from the list.
3.   Reverses these extracted elements.
4.   Prints both the extracted list and the reversed list
5.   # Step 1: Create a list of numbers from 1 to 10
numbers = list(range(1, 11))

# Step 2: Extract the first five elements
first_five = numbers[:5]

# Step 3: Reverse the extracted elements
reversed_list = first_five[::-1]

# Step 4: Print both lists
print("original list:",numbers)
print("Extracted first five elements:", first_five)
print("Reversed extracted elements :", reversed_list)
-------------------------------------------------------------------------------------------------------------------------------------------
Assignment5-Task1:
Task 1: Create a Dictionary of Student Marks

Problem Statement: Write a Python program that:
1.   Creates a dictionary where student names are keys and their marks are values.
2.   Asks the user to input a student's name.
3.   Retrieves and displays the corresponding marks.
4.   If the student’s name is not found, display an appropriate message.
5.   Code:
 Step 1: Create a dictionary of students and their marks
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


 


