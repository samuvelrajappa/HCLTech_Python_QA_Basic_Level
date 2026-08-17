# Get a number from user and check whether the digits are in
# ascending order.
def check_assending(num):
    # Convert the number to a string to easily access individual digits
    num_str = str(num)
    # Check if the digits are in ascending order
    for i in range(len(num_str) - 1):
        if num_str[i] >= num_str[i + 1]:
            return False
    return True

def main():
    number1 = int(input("Enter a number: "))
    print(check_assending(number1))

if __name__ == "__main__":
    main()