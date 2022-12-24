num1 = int(input("Enter the 1st Number: "))
num2 = int(input("Enter the 2nd Number: "))
num3 = int(input("Enter the 3rd Number: "))

if (num1 > num2) and (num1 > num3):
    print(num1, "is a largest number")
elif (num2 > num1) and (num2 > num3):
    print(num2, "is a largest number")
elif (num3 > num1) and (num3 > num2):
    print(num3, "is a largest number")
else:
    print("The numbers are equal")