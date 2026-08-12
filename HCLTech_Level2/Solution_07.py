#  Write a loop program to print the two-digit odd numbers, who’s sum of digits are 7.
for i in range(9, 100, 2):
    if (i // 10) + (i % 10) == 7:
        print(i)