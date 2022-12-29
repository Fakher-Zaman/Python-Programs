import random

print("\n\t~~~~~~~~Welcome to RPS Game~~~~~~~~")

user_score = 0
comp_score = 0
ties = 0

name = input("\nEnter your name here: ")
print('''
Winning Rules:
1. Rock vs Scissor --> Rock Wins!
2. Paper vs Rock --> Paper Wins!
3. Scissor vs Paper --> Scissor Wins!
''')

rounds = int(input("How many rounds you want to play: "))
print("Total Rounds are", rounds)

for n in range(1, rounds+1):
    print("\nRound #", n, ":", end=" ")
    print('''
    Choices are:
    1. Rock
    2. Paper
    3. Scissor
    ''')
    choice = int(input("Enter your choice from 1-3: "))

    while choice > 3 or choice < 1:
        choice = int(input("Enter valid input: "))

    if choice == 1:
        user_choice = "Rock"
    elif choice == 2:
        user_choice = "Paper"
    else:
        user_choice = "Scissor"

    print("The user's choice is", user_choice)
    # print("Now it is computer's turn")

    comp = random.randint(1, 3)

    if comp == 1:
        comp_choice = "Rock"
    elif comp == 2:
        comp_choice = "Paper"
    else:
        comp_choice = "Scissor"

    print("The computer's choice is", comp_choice)

    if ((user_choice == "Paper" and comp_choice == "Rock") or (user_choice == "Rock" and comp_choice == "Paper")):
        print("Paper Wins!")
        result = "Paper"
    elif ((user_choice == "Rock" and comp_choice == "Scissor") or (user_choice == "Scissor" and comp_choice == "Rock")):
        print("Rock Wins!")
        result = "Rock"
    elif ((user_choice == "Paper" and comp_choice == "Scissor") or (user_choice == "Scissor" and comp_choice == "Paper")):
        print("Scissor Wins!")
        result = "Scissor"
    else:
        print("It's a Tie!")
        result = "Tie"

    if (result == user_choice or result == "Tie"):
        user_score += 1
    if (result == comp_choice or result == "Tie"):
        comp_score += 1
    if (result == "Tie"):
        ties += 1

print("\a\n")
if user_score > comp_score:
    print("User Wins!", "and Score =", user_score)
elif user_score < comp_score:
    print("Computer Wins!", "and Score =", comp_score)
elif user_score == comp_score:
    print(f'''  Game Tie!
                User Score = {user_score}
                Computer Score = {comp_score} ''')
else:
    print("Something Went Wrong!")

print("Total Ties =", ties)