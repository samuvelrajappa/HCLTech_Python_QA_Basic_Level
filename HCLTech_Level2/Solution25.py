# Write a program get number from user print the total number of 
# single-digit prime numbers in the number
num = input("Enter a long digit number: ")
count = 0
single_digit_primes = {2, 3, 5, 7}  # Single-digit prime numbers
for digit in num:
    if int(digit) in single_digit_primes:
        count += 1
print("Total single-digit prime numbers in the number are:", count)