# Display Powers of 2 Using Anonymous (Lambda) Function.

nterms = int(input("Enter the number of power: "))

result = list(map(lambda x : 2 ** x, range(nterms+1)))

print(result)   # In the form of list

for i in range (nterms + 1):
    print("The value of 2 raised to the power of", i, "is", result[i])
