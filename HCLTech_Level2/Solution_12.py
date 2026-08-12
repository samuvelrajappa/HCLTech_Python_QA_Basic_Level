# Write a program to get a number from user and print the sum of all digits
num = input("Enter a number: ")
sum_of_digits = 0
for digit in num:
    sum_of_digits += int(digit)
print("Sum of all digits in the number is:", sum_of_digits)