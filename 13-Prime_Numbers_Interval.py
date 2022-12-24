# Python program to print all prime numbers in an interval:
lower = int(input("Enter the lower number: "))
upper = int(input("Enter the upper number: "))

print("The prime numbers are:")
for num in range(lower, upper+1):
    if(num > 1):
        for iterate in range(2, num):
            if(num % 2 == 0):
                break
        else:
            print(num)

    else:
        print("Please enter the number greater than 1")
        break