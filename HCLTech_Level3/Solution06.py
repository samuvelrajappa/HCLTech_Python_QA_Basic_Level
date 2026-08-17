# Get a number from user and reverse that number and print. 
# Write your code inside the function. 
# Do not Change the format.
def reverse_number(number):
    # Your Program Here
    reversed_number = int(str(number)[::-1])
    return reversed_number
def main():
    number = int(input("Enter a number: "))
    result = reverse_number(number)
    print(f"The reversed number (assuming reverse_number works) would be: {result}")

if __name__ == "__main__":
    main()