#  Write a program to print the total count of numbers which are 
# less than 100000 and whose sum of digits is 14
num = int(input("Enter a number: "))
count = 0
for i in range(num):
    if i < 100000:
        sum_of_digits = sum(int(digit) for digit in str(i))
        if sum_of_digits == 14:
            count += 1
print("Total count:", count)
