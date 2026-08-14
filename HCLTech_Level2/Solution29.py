# Write a program to get three numbers from user and print the 
# LCM of those numbers.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
if num1 > num2 and num1 > num3:
    greater = num1
elif num2 > num1 and num2 > num3:
    greater = num2
else:
    greater = num3
while True:
    if greater % num1 == 0 and greater % num2 == 0 and greater % num3 == 0:
        lcm = greater
        break
    greater += 1
print("LCM of", num1, ",", num2, "and", num3, "is", lcm)