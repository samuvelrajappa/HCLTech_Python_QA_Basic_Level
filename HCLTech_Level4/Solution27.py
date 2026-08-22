# Print the largest three-digit prime number
for num in range(999, 99, -1):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print("Largest three-digit prime number:", num)
        break