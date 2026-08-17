# Get two numbers from user and compare the numbers. 
# If same print “Same” otherwise print “Not Same”. 
# Write your code inside the function. 
# Do not Change the format.
def function(no1):
    no2 = int(input("Enter another number: "))
    # Your Program Here
    if no1 == no2:
        return "Same"
    else:
        return "Not Same"
    
def main():
    number1 = int(input("Enter a number: "))
    number2 = function(number1)
    print(number2)

if __name__ == "__main__":
    main()
