# Solution no. 1 (By using 3rd variable):
x = int(input("Enter a number for x: "))
y = int(input("Enter a number for y: "))

temp = 0

# Swapping
temp = x
x = y
y = temp

print("The value of x = ", x)
print("The value of y = ", y)

# Solution no. 1 (By using law):
x = int(input("Enter a number for x: "))
y = int(input("Enter a number for y: "))

# Swapping
x, y = y, x

print("The value of x = ", x)
print("The value of y = ", y)