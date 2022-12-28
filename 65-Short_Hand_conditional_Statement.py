# ---> Python Shorthand: If and If-Else Statement using Python

num = int(input("Enter a number: "))
# Simple Method:
if num % 2 == 0:
    print("It is Even")
# Shorthand Method:
if num % 2 == 0: print("It is Even")

#------------------------------------------

# Simple Method:
if num % 2 == 0:
    print("EVEN")
else:
    print("ODD")
# Shorthand Method:
print("EVEN") if num % 2 == 0 else print("ODD")