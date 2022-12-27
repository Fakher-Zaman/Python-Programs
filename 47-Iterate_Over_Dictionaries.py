# Program to iterate over dictionaries using for loop:
friends = {578: "Fakher Zaman", 582: "Hammad Asif", 552: "Muhammad Shaban"}

print("SOlution # 1(By using .items() Method)")
for key, value in friends.items():
    print(key, ":", value)

print("\nSOlution # 2(By using key value)")
for key in friends:
    print(key, ":", friends[key])