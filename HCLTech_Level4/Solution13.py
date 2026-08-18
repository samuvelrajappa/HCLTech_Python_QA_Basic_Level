# Get a number from the user and print the sum of all digits
number = int(input("Enter a number:"))
con = str(number)
store = 0
for i in range(len(con)):
    store += int(con[i])
print("Sum of all digit:", store)