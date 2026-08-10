n = int(input("Enter a number: "))
store = 0
for i in range(1, n + 1):
    store += i
    print(i)
print("Sum:", store)