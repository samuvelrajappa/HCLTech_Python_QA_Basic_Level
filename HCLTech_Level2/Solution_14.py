#  Write a program to get a number from user and interchange the first and last digits and print the result.
num = input("Enter a number: ")
if len(num) < 2:
    print("Number must have at least two digits.")
else:
    first_digit = num[0]
    last_digit = num[-1]
    middle_part = num[1:-1]
    new_num = last_digit + middle_part + first_digit
    print("Number after interchanging first and last digits:", new_num)