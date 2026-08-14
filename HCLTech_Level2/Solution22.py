#  Write a program get number from user print the total number 
# of two-digit odd numbers in the number
num = input("Enter a long digit number: ")
count = 0
for i in range(len(num) - 1):
    two_digit_num = int(num[i:i + 2])
    if two_digit_num % 2 != 0:
        count += 1
print("Total two-digit odd numbers in the number are:", count)