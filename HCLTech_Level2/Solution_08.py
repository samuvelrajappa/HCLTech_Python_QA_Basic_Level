#  Write a loop program to print the two-digit even numbers, who’s sum of digits are 6.
for i in range(10, 100, 2):
    if (i // 10) + (i % 10) == 6:
        print(i)