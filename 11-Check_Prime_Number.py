num = int(input("Enter a Number: "))

if num <= 1:
    print(num, "is not a prime number.")

elif num > 1:
    for iterate in range(2, num):
        if num % iterate == 0:
            print(num, "is not a prime number.")
            break
    else:
        print(num, "is a prime number.")

else:
    print("Something Went Wrong!")