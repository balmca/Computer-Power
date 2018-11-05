import random as random
user = True

# Welcome and Instructions
print("Welcome to Paper, Scissors, Rock - you're up against HAL, the Computer!")

while True:
    # Options and HAL
    options = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}
    HAL = random.choice(list(options))
    # User Input and Exit
    user = raw_input("\nEnter Paper (P), Scissors (S), Rock (R), or Exit (E): ")
    user = user.lower()
    if user == 'e':
        print("End Game")
        break
    elif user == 'r':
        print("Your choice: " + options[user])
        print("HAL's choice: " + options[HAL])
        if HAL == 'r':
            print("Its a draw!")
        elif HAL == 'p':
            print("HAL Wins!")
        else:
            print("You Win!")
    elif user == 'p':
        print("Your choice: " + options[user])
        print("HAL's choice: " + options[HAL])
        if HAL == 'r':
            print("You Win!")
        elif HAL == 'p':
            print("Its a draw!")
        else:
            print("HAL Wins!")
    elif user == 's':
        print("Your choice: " + options[user])
        print("HAL's choice: " + options[HAL])
        if HAL == 'r':
            print("HAL Wins!")
        elif HAL == 'p':
            print("HAL Wins!")
        else:
            print("Its a draw!")
    else:
        print("\nThat's made up, this is Paper, Scissors, Rock!")
