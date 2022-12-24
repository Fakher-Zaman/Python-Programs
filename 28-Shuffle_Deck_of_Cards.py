import random, itertools

deck = list(itertools.product(range(1, 14), ["Spade", "Club", "Hearts", "Diamond"]))

# print("Before Shuffle", deck)
random.shuffle(deck)
print("\nAfter Shuffle:\n", deck, "\n")

for i in range(53):
    print(deck[i][0], "of", deck[i][1])