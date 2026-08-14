# Write a program print total number of single digit Prime numbers
count = 0
for i in range(1, 10):
    if i > 1:
        for j in range(2, int(i**0.5) + 1):
            if (i % j) == 0:
                break
        else:
            count += 1
            print(i, "is a prime number")
print("Total number of single digit prime numbers:", count)