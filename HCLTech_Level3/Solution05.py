# Get a number from user and count the number of zeros in that number and print. 
# Write your code inside the function. 
# Do not Change the format.
def find_number_of_zeros(number):
    count_of_zeros = str(number).count('0')
    return count_of_zeros
number = int(input("Enter a number: "))  
result = find_number_of_zeros(number)
print(result)