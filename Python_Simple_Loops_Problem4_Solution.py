n = int(input("Enter a number: "))
store = 0
for i in range(n, 0, -1):
    store += i
    print(i)
print("Sum:", store)