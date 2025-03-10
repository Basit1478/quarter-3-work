#bitwise operators
# & - AND
a = 5        # 0101
b = 3        # 0011
result = a & b
print(result)  # 1 (0001)

# | - OR
a = 5        # 0101
b = 3        # 0011
result = a | b
print(result)  # 7 (0111)

# ^ - XOR
a = 5        # 0101
b = 3        # 0011
result = a ^ b
print(result)  # 6 (0110)

# ~ - NOT
a = 5        # 0101
result = ~a
print(result)  # -6 (in binary: flips all bits, in two’s complement form)

# << - LEFT SHIFT
a = 5        # 0101
result = a << 1
print(result)  # 10 (1010)

# >> - RIGHT SHIFT
a = 5        # 0101
result = a >> 1
print(result)  # 2 (0010)

