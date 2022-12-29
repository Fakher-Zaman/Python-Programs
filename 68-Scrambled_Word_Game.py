# Anagrams Game: Build a Scrambled Word Game
import random

# words = ["ironman", "thor", "hawkeye", "wanda", "vision"]
File = open("68-words.txt", "r")
a = File.readline()
words = a.split(",")
print(words)

word = random.choice(words)
print(word)

jumble = "".join(random.sample(word, len(word)))
# print(jumble)

chances = 3

print("~"*40)
print("~~~~~~~~ Avengers Jumble Bumble ~~~~~~~~")
print("~"*40)

while chances != 0:
    print("The word is", jumble)
    guess = input("Enter your guessed word: ").lower()
    if guess == word:
        print("Correct Guess!")
        print("You Won!")
    else:
        chances -= 1
        print("Incorrect Guess!")
        print("Remaining chances are:", chances)
        print("")

else:
    print("All your chances are exhasted")
    print("You Lose")
    print("The correct word is", word)

print("Thank You For Playing!")