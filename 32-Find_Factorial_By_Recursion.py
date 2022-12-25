def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return (n * fact(n-1))

num = int(input("Enter a Number: "))

if num < 0:
    print("Factorial of number less than 1 does not exist!")
else:
    print("The factorial of", num, "=", fact(num))