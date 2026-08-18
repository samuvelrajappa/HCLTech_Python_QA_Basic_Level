# Write a program to print the total number of
# single digit Prime numbers. Assume 0 & 1 are not Prime.
count = 0
for num in range(2, 10):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        count += 1

print("Total number of single digit prime numbers:", count)