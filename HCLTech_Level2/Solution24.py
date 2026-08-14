# Write a program get number from user print the total number 
# of two-digit perfect square numbers in the number.
num = input("Enter a long digit number: ")
count = 0
perfect_squares = {16, 25, 36, 49, 64, 81}  # Two-digit perfect squares
for i in range(len(num) - 1):
    two_digit_num = int(num[i:i + 2])
    if two_digit_num in perfect_squares:
        count += 1
print("Total two-digit perfect square numbers in the number are:", count)