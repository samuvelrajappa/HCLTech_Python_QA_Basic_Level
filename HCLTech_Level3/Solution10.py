# Get a number from user, 
# find the number of digits and print the same.
def count_Digits(num):
    num_str = str(num)
    return len(num_str)

def main():
    number1 = int(input("Enter a number: "))
    print(count_Digits(number1))
if __name__ == "__main__":
    main()