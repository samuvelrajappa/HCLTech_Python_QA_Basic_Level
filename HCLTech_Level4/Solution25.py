# Program to Print the sum of all THREE digit Prime numbers.
count = 0
for num in range(100, 1000):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        count += num

print("Sum of three digit prime numbers:", count)