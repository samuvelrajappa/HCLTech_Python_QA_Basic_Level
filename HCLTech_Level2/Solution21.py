# Write a program get number from user print the total number 
# digits which are odd in the number
num = input("Enter a long digit number: ")
count = 0
for digit in num:
    if int(digit) % 2 != 0:
        count += 1
print("Total odd digits in the number are:", count)