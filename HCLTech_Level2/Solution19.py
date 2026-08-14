#  Write a program to get a 4-digit number from user, print whether 
# that number’s middle two digits (hundred’s digit and ten’s digit) is prime
get = input("Enter a 4-digit number: ")
num = int(get[-3:-1])
if num > 1:
    for i in range(2, int(num**0.5) + 1):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")