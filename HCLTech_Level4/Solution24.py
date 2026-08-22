# Program to print the sum of all TWO digit Prime numbers
count = 0
for num in range(10, 100):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        count += num

print("Sum of two digit prime numbers:", count)