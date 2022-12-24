num = int(input("Enter a number: "))
fact = 1

# Solution # 1 (By Simple Method):
# if num < 0:
#     print("The factorial of", num, "does'nt exist")

# elif num == 0:
#     print("The factorial of", num, "is 1")

# else:
#     for i in range(1, num+1):
#         fact = fact * i
#     print("The factorial of", num, "is equal to", fact)

# Solution # 2 (By Recursion Method):
def factorial(n):
    if n == 0:
        return 1
    else:
        return ((n)*factorial(n-1))

result = factorial(num)
print("The factorial of", num, "is equal to", result)
