print("~~~~~~~~Mini Calculator~~~~~~~")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

choice = str(input("Press the operation from (+, -, *, /): "))

if choice == '+':
    print("The addition of both numbers =", int(num1 + num2))
elif choice == '-':
    print("The addition of both numbers =", int(num1 - num2))
elif choice == '*':
    print("The addition of both numbers =", int(num1 * num2))
elif choice == '/':
    print("The addition of both numbers =", int(num1 / num2))
else:
    print("Invalid Input!")