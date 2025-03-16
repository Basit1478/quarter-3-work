#1 Creating a Set

# Creating a set with curly braces
my_set = {1, 2, 3, 4, 5}
print(my_set)

# Creating a set using the set() constructor
another_set = set([1, 2, 3, 4, 5, 5, 5])
print(another_set)  # Duplicate 5 is removed

# Empty set (note: {} creates an empty dictionary)
empty_set = set()
print(empty_set)


#2 Adding Elements

my_set = {1, 2, 3}
my_set.add(4)
print(my_set)  # {1, 2, 3, 4}

# Adding multiple items (iterable) at once
my_set.update([5, 6])
print(my_set)  # {1, 2, 3, 4, 5, 6}


#3 Removing Elements 

my_set = {1, 2, 3, 4, 5}

my_set.remove(3)  # Raises KeyError if element not found
print(my_set)  # {1, 2, 4, 5}

my_set.discard(2)  # Doesn't raise error if element not found
print(my_set)  # {1, 4, 5}

# Remove and return a random element
popped = my_set.pop()
print(popped)     # Random item (e.g., 1)
print(my_set)     # Remaining set


#4 Set Operations

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Union (combines both sets without duplicates)
print(A | B)                # {1, 2, 3, 4, 5, 6}
print(A.union(B))           # {1, 2, 3, 4, 5, 6}

# Intersection (common elements)
print(A & B)                # {3, 4}
print(A.intersection(B))    # {3, 4}

# Difference (elements in A but not in B)
print(A - B)                # {1, 2}
print(A.difference(B))      # {1, 2}

# Symmetric Difference (elements in A or B but not both)
print(A ^ B)                        # {1, 2, 5, 6}
print(A.symmetric_difference(B))    # {1, 2, 5, 6}


#5 Other Useful Methods

# Check membership
print(1 in A)  # True
print(5 in A)  # False

# Length of a set
print(len(A))  # 4

# Clear all items
A.clear()
print(A)       # set()


#6 Example Use Case: Removing Duplicates from a List

numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers)
print(unique_numbers)  # {1, 2, 3, 4, 5}

