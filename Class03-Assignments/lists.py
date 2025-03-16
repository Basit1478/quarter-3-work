#1 creating a list

# List of integers
numbers = [10, 20, 30, 40]

# List of strings
fruits = ['apple', 'banana', 'cherry']

# Mixed data types
mixed = [1, "hello", 3.14, True]


#2 Accessing Elements

fruits = ['apple', 'banana', 'cherry']

# Access by index (starts at 0)
print(fruits[0])  # Output: apple
print(fruits[2])  # Output: cherry

# Negative indexing
print(fruits[-1])  # Output: cherry (last element)


#3 Modifying a list

fruits = ['apple', 'banana', 'cherry']

# Change an item
fruits[1] = 'blueberry'
print(fruits)  # ['apple', 'blueberry', 'cherry']


#4 Adding Elements

numbers = [1, 2, 3]

# Append - adds to the end
numbers.append(4)
print(numbers)  # [1, 2, 3, 4]

# Insert - adds at specific position
numbers.insert(1, 10)
print(numbers)  # [1, 10, 2, 3, 4]

# Extend - adds multiple elements
numbers.extend([5, 6])
print(numbers)  # [1, 10, 2, 3, 4, 5, 6]


#5 Removing Elements

fruits = ['apple', 'banana', 'cherry', 'banana']

# Remove by value (removes first occurrence)
fruits.remove('banana')
print(fruits)  # ['apple', 'cherry', 'banana']

# Remove by index
del fruits[1]
print(fruits)  # ['apple', 'banana']

# Pop - removes and returns the last item (or by index)
last_fruit = fruits.pop()
print(last_fruit)  # banana
print(fruits)      # ['apple']


#6 Looping Through a List

fruits = ['apple', 'banana', 'cherry']

# Simple for loop
for fruit in fruits:
    print(fruit)

# Using index
for i in range(len(fruits)):
    print(i, fruits[i])


#7 List Comprehension (Quick way to create lists)

# Create a list of squares
squares = [x**2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]

# Filter even numbers
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8]


#8 Sorting and Reversing

numbers = [5, 2, 9, 1]

# Sort in ascending order
numbers.sort()
print(numbers)  # [1, 2, 5, 9]

# Sort in descending order
numbers.sort(reverse=True)
print(numbers)  # [9, 5, 2, 1]

# Reverse the list (doesn't sort)
numbers.reverse()
print(numbers)  # [1, 2, 5, 9]


#9 Other Useful Functions

numbers = [1, 2, 3, 4, 5]

# Length of list
print(len(numbers))  # 5

# Check if element exists
print(3 in numbers)  # True

# Count occurrences
print(numbers.count(2))  # 1

# Index of an element
print(numbers.index(4))  # 3


#10 Nested Lists

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Access 5
print(matrix[1][1])  # 5

# Loop through rows
for row in matrix:
    print(row)

# Flatten nested list (advanced)
flat = [num for row in matrix for num in row]
print(flat)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
