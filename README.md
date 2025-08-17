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

