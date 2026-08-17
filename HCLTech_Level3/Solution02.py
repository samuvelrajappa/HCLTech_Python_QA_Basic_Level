# Get a number from user and subtract 5 to that number and print the result. 
# Write your code inside the function.
def function(no1):
    no2 = 0
    # Your Program Here
    no2 = no1 - 5
    return no2
def main():
    number1 = int(input("Enter a number: "))
    number2 = function(number1)
    print(number2)
if __name__ == "__main__":
    main()