import random as random
user = True

# Welcome and Instructions
print("\nWelcome to Paper, Scissors, Rock - you're up against HAL, the Computer!")


while True:
    # Options and HAL
    options = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors', 'e': 'Exit'}
    HAL = random.choice(list(options))
    while HAL == 'e':
        HAL = random.choice(list(options))
    # User Input and Exit
    user = raw_input("\nEnter Paper (P), Scissors (S), Rock (R), or Exit (E): ").lower()
    if user == 'e':
        print("End Game")
        break
    elif user == 'r':
        print("Your choice: " + options[user])
        print("HAL's choice: " + options[HAL])
        if HAL == 'p':
            print("HAL Wins!")
        elif HAL == 's':
            print("You Win!")
        else:
            print("Draw!")
    elif user == 'p':
        print("Your choice: " + options[user])
        print("HAL's choice: " + options[HAL])
        if HAL == 'r':
            print("You Win!")
        elif HAL == 's':
            print("HAL Wins!")
        else:
            print("Draw!")
    elif user == 's':
        print("Your choice: " + options[user])
        print("HAL's choice: " + options[HAL])
        if HAL == 'r':
            print("HAL Wins!")
        elif HAL == 'p':
            print("You Win!")
        else:
            print("Its a draw!")
    else:
        print("\nThat's made up, this is Paper, Scissors, Rock!")
