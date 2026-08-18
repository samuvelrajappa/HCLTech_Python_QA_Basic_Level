# Write a program to print the total number of 
# TWO digit odd numbers.
count = 0
for i in range(10,100):
    if i % 2 != 0:
        count += 1
print("Total number of two digit odd number:",count)