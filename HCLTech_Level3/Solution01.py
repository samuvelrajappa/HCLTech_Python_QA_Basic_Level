# Get a number from user and add 2 to that number and print the result. 
# Write your code inside the function. 
# Do not Change the Code.
def function(no1):
    # Define and initialize no2
    no2 = 0
    # Your Program Here
    no2 = no1 + 2
    return no2
    
def main():
    number1 = int(input("Enter a number: "))
    number2 = function(number1)
    print(number2)

if __name__ == "__main__":
    main() 