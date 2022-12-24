num = int(input("Enter a Number: "))

if num < 0:
    print("Please Enter Positive Number:")
else:
    sum = 0
    n = num
    while num > 0:
        sum += num
        num -= 1
    print("The sum of first", n, "natural numbers:", sum)