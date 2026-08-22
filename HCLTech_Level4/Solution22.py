# Write a program to print total number of THREE digit Prime numbers.
count = 0
for num in range(100, 1000):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        count += 1

print("Total number of three digit prime numbers:", count)