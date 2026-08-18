# Write a program to print the sum of all TWO digit odd numbers.
count = 0
for i in range(10,100):
    if i % 2 != 0:
        count += i
print("Total number of two digit odd number:",count)