''' Write a program to get a number from user, print whether that 
number is prime, and sum of digit is equal to 14. '''
num = int(input("Enter a number: "))
con = str(num)
sum_of_digits = sum(int(digit) for digit in con)
if num > 1:
    for i in range(2, int(num**0.5) + 1):
        if (num % i) == 0:
            print(num, "is not a prime number & sum of digits is", sum_of_digits)
            break
    else:
        print(num, "is a prime number & sum of digits is", sum_of_digits)
else:
    print(num, "is not a prime number & sum of digits is", sum_of_digits)