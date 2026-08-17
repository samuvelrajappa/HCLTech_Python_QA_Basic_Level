# Get a two-digit number from user swap the digits.
def swapNumbers(num):
    num_str = str(num)
    swapped_str = num_str[1] + num_str[0]
    return int(swapped_str)

def main():
    number1 = int(input("Enter a two-digit number: "))
    print(swapNumbers(number1))
if __name__ == "__main__":
    main()