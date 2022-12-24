lower = int(input("Enter the lower limit here: "))
upper = int(input("Enter the upper limit here: "))

print("The armstrong numbers in the range of", lower, "to", upper, ":")
for num in range (lower, upper+1):
    sum = 0
    order = len(str(num))
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10
    if num == sum:
        print(num)