#1 Creating a tuple

# A tuple of integers
numbers = (1, 2, 3, 4)

# A tuple with mixed data types
mixed = ("hello", 3.14, 42)

# A tuple inside a tuple (nested)
nested = (1, 2, (3, 4))

# Single-element tuple (note the comma!)
single_element = (5,)


#2 Accessing Elements

my_tuple = ('apple', 'banana', 'cherry')

print(my_tuple[0])  # Output: apple
print(my_tuple[1])  # Output: banana


#3 Slicing Tuples

my_tuple = (10, 20, 30, 40, 50)

print(my_tuple[1:4])  # Output: (20, 30, 40)


#4 Looping Through a Tuple

fruits = ('apple', 'banana', 'cherry')

for fruit in fruits:
    print(fruit)


#5 Tuple Unpacking

person = ("John", 25, "Engineer")

name, age, profession = person

print(name)       # Output: John
print(age)        # Output: 25
print(profession) # Output: Engineer


#6 Immutability (Tuples can't be changed!)

my_tuple = (1, 2, 3)

# This will raise an error!
# my_tuple[0] = 10
# TypeError: 'tuple' object does not support item assignment


#7 Tuple Methods

my_tuple = (1, 2, 3, 2, 2, 4)

print(my_tuple.count(2))  # Output: 3 (counts how many times 2 appears)
print(my_tuple.index(3))  # Output: 2 (first index where 3 appears)


#8 Tuples Are Faster Than Lists (Performance Example)

import timeit

# Compare execution time of creating lists vs tuples
print(timeit.timeit(stmt="(1, 2, 3, 4, 5)", number=1000000))  # Faster
print(timeit.timeit(stmt="[1, 2, 3, 4, 5]", number=1000000))  # Slower
