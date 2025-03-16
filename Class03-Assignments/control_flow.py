#Conditional Statements
score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")

#loops
#for loop
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

#while loop
count = 0

while count < 5:
    print("Count is:", count)
    count += 1

#control statements
for num in range(10):
    if num == 3:
        continue  # skip this number
    if num == 7:
        break  # stop the loop
    if num == 5:
        pass # stop the loop
    print(num)

