# Write a program to get number from user, print whether that 
# number’s first two digits (ten’s digits and one’s digit) is prime.
get = input("Enter numbers < 10: ")
num = int(get[-2:])
if num > 1:
    for i in range(2, int(num**0.5) + 1):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")