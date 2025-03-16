#1 Creating a Dictionary

# Example 1: Empty dictionary
my_dict = {}

# Example 2: With some data
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}


#2 Accessing Values

#You use the key to get a value.


print(person["name"])  # Output: Alice
print(person.get("age"))  # Output: 25

#.get() is safer—returns None (or default) if the key doesn’t exist.

print(person.get("country", "Not Found"))  # Output: Not Found


#3 Adding / Updating Items

# Add a new key-value pair
person["job"] = "Engineer"

# Update an existing value
person["age"] = 26

print(person)
# Output: {'name': 'Alice', 'age': 26, 'city': 'New York', 'job': 'Engineer'}


#4 Removing Items

# Remove a key-value pair by key
person.pop("city")

# Or use del
del person["job"]

print(person)
# Output: {'name': 'Alice', 'age': 26}


#5 Looping Through a Dictionary

# Loop through keys
for key in person:
    print(key, person[key])

# Loop through key-value pairs
for key, value in person.items():
    print(f"{key} => {value}")


#6 Dictionary Methods Cheat Sheet
# Method	    Description

#.keys()	    Returns all keys
#.values()	    Returns all values
#.items()	    Returns key-value pairs
#.get(key)	    Returns value of key (or None)
#.update()	    Updates dictionary with another dictionary
#.pop(key)	    Removes key and returns value
#.clear()	    Removes all items


#7 Nested Dictionary

students = {
    "101": {"name": "Alice", "grade": "A"},
    "102": {"name": "Bob", "grade": "B"},
}

print(students["101"]["name"])  # Output: Alice


#Example Use Case

# Count the number of times each letter appears in a word
word = "hello"
letter_count = {}

for letter in word:
    if letter in letter_count:
        letter_count[letter] += 1
    else:
        letter_count[letter] = 1

print(letter_count)
# Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}
