# Find the Sum of Natural Numbers Using Recursion

def Natural_Number_Sum(n):
    if n <= 1:
        return n
    else:
        return n + Natural_Number_Sum(n-1)

num = int(input("Enter a Number: "))

if num <= 0:
    num = print("Enter a positive number: ")
else:
    print("The sum of first N natural numbers: ", Natural_Number_Sum(num))