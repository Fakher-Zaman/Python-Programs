# Program to Sort a Dictionary by Value

# Solution # 1:
print("Before Sorting: ")
friends = {578: "Fakher Zaman", 582: "Hammad Asif", 552: "Muhammad Shaban"}
print(friends)

print("\nAfter Sorting: ")
sortedValue = sorted(friends.items(), key = lambda x : x[0])
print(sortedValue)