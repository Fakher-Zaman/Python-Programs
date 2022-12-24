def findHCF(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    
    for i in range(1, smaller+1):
        if(x % i == 0) and (y % i == 0):
            hcf = i
    return hcf

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print("The HCF of the given two number is", findHCF(a, b))