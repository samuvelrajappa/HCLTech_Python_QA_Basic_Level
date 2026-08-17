# Get a number from user and Check Prime or Not and print the result. 
# Write your code inside the function. Do not Change the format.
def is_prime(number):
    """Placeholder function for checking 
    prime numbers (logic not implemented)"""
    if number <= 1:
        return False
    
    else:
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
    return True

def main():
    """Placeholder function for getting input 
    and checking primeness (logic not implemented)"""
    number = int(input("Enter a number: "))  # Example number (replace with your logic to get input)
    result = is_prime(number)
    if result:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")

if __name__ == "__main__":
    main()