def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y

num1Unit = input("What are the units for the first number?: ")


#buttons
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

b = 8
kb = 1024
mb = 1024
gb = 1024





#the calculation
while True:
    choice = input("Enter 1,2,3 or 4: ")
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1,num2), num1Unit)

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2), num1Unit)

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2), num1Unit)

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2), num1Unit)
        break
    else:
        print("Invalid Input")