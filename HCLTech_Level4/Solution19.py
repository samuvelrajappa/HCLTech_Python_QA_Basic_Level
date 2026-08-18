# Write a program to print the sum of all THREE digit odd numbers
count = 0
for i in range(100,1000):
    if i % 2 != 0:
        count += i
print("Total number of three digit odd number:",count)