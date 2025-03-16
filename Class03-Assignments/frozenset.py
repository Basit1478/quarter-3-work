#1 Creating a Frozenset

# Empty frozenset
empty_fs = frozenset()
print(empty_fs)  # frozenset()

# From a list
fs_list = frozenset([1, 2, 3])
print(fs_list)  # frozenset({1, 2, 3})

# From a tuple
fs_tuple = frozenset((4, 5, 6))
print(fs_tuple)  # frozenset({4, 5, 6})

# From a string (characters are unique)
fs_string = frozenset("hello")
print(fs_string)  # frozenset({'e', 'h', 'l', 'o'})


#2 Membership test

fs = frozenset([1, 2, 3, 4])

print(3 in fs)  # True
print(5 in fs)  # False


#3 Iterating Over a frozenset

fs = frozenset([10, 20, 30])

for item in fs:
    print(item)


#4 Union of Two frozensets

fs1 = frozenset([1, 2, 3])
fs2 = frozenset([3, 4, 5])

result = fs1.union(fs2)
print(result)  # frozenset({1, 2, 3, 4, 5})


#5 Intersection of Two frozensets

fs1 = frozenset([1, 2, 3])
fs2 = frozenset([2, 3, 4])

result = fs1.intersection(fs2)
print(result)  # frozenset({2, 3})


#6 Difference B/W Two frozensets

fs1 = frozenset([1, 2, 3, 4])
fs2 = frozenset([3, 4, 5])

result = fs1.difference(fs2)
print(result)  # frozenset({1, 2})


#7 Symmetric Difference

fs1 = frozenset([1, 2, 3])
fs2 = frozenset([3, 4, 5])

result = fs1.symmetric_difference(fs2)
print(result)  # frozenset({1, 2, 4, 5})


#8 Check Subset / Superset / Disjoint

a = frozenset([1, 2])
b = frozenset([1, 2, 3])
c = frozenset([4, 5])

print(a.issubset(b))      # True
print(b.issuperset(a))    # True
print(a.isdisjoint(c))    # True


#9 Using frozenset as Dictionary Keys

fs1 = frozenset([1, 2])
fs2 = frozenset([3, 4])

my_dict = {
    fs1: "first group",
    fs2: "second group"
}

print(my_dict[frozenset([1, 2])])  # first group


#10 frozenset in a Set (Nested Sets)


fs1 = frozenset([1, 2])
fs2 = frozenset([3, 4])

nested_set = {fs1, fs2}

print(nested_set)  # {frozenset({1, 2}), frozenset({3, 4})}


#11  Real-World Example: Representing Graph Edges

# Graph edges as frozensets
edges = {
    frozenset(["A", "B"]): 5,  # weight 5
    frozenset(["B", "C"]): 3
}

# Access an edge weight regardless of order
print(edges[frozenset(["B", "A"])])  # 5


#12 Hashability (for Advanced Use)

fs = frozenset([1, 2, 3])
print(hash(fs))  # Unique hash value


#13 Invalid Mutating Operations

#These methods don't exist on frozenset:

fs = frozenset([1, 2, 3])

# These will raise AttributeError:
# fs.add(4)
# fs.remove(1)
# fs.clear()
# fs.pop()

#Example:

try:
    fs.add(4)
except AttributeError as e:
    print(e)  # 'frozenset' object has no attribute 'add'

    #14 Copying a Frozenset

    fs = frozenset([1, 2, 3])

copy_fs = fs.copy()
print(copy_fs)  # frozenset({1, 2, 3})
