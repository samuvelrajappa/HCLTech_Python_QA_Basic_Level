# Write a program to print the sum of all single digit odd numbers.
count = 0
for i in range(1,10):
    if i % 2 != 0:
        count += i
print("Sum of single digit odd number:",count)