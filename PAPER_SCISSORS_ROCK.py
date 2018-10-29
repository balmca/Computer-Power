import random
user = True

# Options and HAL
options = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors', 'e': 'Exit'}
HAL = random.choice(list(options))

# Welcome and Instructions
print("Welcome to Paper, Scissors, Rock - you're up against HAL, the Computer!")

# User Input and Exit
while True:
    user = input("Enter Paper (P), Scissors (S), Rock (R), or Exit (E): ")
    user = user.lower()
    if user == 'e':
        print("End Game")
        break
    if user == 'r':
        print("HAL's choice:", HAL)
        if HAL == 'r':
            print("Its a draw!")
        elif HAL == 'p':
            print("HAL Wins!")
        else:
            print("You Win!")
    if user == 'p':
        print("HAL's choice:", HAL)
        if HAL == 'r':
            print("You Win!")
        elif HAL == 'p':
            print("Its a draw!")
        else:
            print("HAL Wins!")
    if user == 's':
        print("HAL's choice:", HAL)
        if HAL == 'r':
            print("HAL Wins!")
        elif HAL == 'p':
            print("HAL Wins!")
        else:
            print("Its a draw!")
    else:
        print("That's made up, this is Paper, Scissors, Rock!")

