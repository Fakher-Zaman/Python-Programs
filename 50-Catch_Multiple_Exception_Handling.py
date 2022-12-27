# Catch Multiple Exception Handling in Python - One Line Program:

string = input("Enter a string here: ")
try:
    num = int(input("Enter a string here: "))
    print(string + num)
except(ValueError, TypeError) as a:
    print(a)