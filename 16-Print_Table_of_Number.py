num = int(input("Enter a number: "))

print("------------- Table of", num, "-------------")

# Solution # 1 (By Using For Loop)
# for i in range(1, 11):
#     print(num, "x", i, "=", (num*i))

# Solution # 1 (By Using While Loop)
i = 1
while i <= 10:
    print(num, "x", i, "=", (num*i))
    i += 1