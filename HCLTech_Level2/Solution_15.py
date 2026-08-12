'''Write a program to get a number from user and if the last digit of 
the number is even print the same number. If the last digit of the number is 
odd then subtract 1 from the last digit and print the number.
(Note: Last digit -MSB) '''
num = input("Enter a number: ")
last_digit = int(num[-1])
if last_digit % 2 == 0:
    print("The number is:", num)
else:
    new_last_digit = last_digit - 1
    new_num = num[:-1] + str(new_last_digit)
    print("The number after subtracting 1 from the last digit is:", new_num)