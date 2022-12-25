def bin_to_dec(n):
    if n > 1:
        (bin_to_dec(n // 2))
    print (n % 2, end=" ")

num = int(input("Enter a Number: "))

print("The Binary of", num, ":")
bin_to_dec(num)