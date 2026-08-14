#  Write a program get number from user print the total number 
# of single-digit perfect square numbers in the number.
num = input("Enter a long digit number: ")
count = 0
perfect_squares = {0, 1, 4, 9}  # Single-digit perfect squares
for digit in num:
    if int(digit) in perfect_squares:
        count += 1
print("Total single-digit perfect square numbers in the number are:", count)