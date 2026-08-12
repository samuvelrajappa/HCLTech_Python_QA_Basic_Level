# Write a loop program to print the sum of two-digit odd numbers, whose ten’s digit is 7.
sum = 0
for i in range(71, 80, 2):
    sum += i
print("Sum of two-digit odd numbers whose ten's digit is 7:", sum)