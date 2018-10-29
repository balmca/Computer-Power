# Welcome message
print ("Welcome to BINGO!")

print ("Instructions: You will have 10 slots to fill on your BINGO card, which contains random numbers between 1 and 80.")
print ("Each round a random number will be brought out and you can check it against your BINGO card!")


guess = ['7', '14', '26', '22', '40', '34', '58', '55', '73', '68']

# Guess
while True:
    guess = int(input("Enter a number between 1 and 80:"))
    if guess == '7':
        guess.remove ('7')
        print("You got one!")
    if guess == '14':
        guess.remove ('14')
        print("You got one!")
    if guess == '26':
        guess.remove ('26')
        print("You got one!")
    if guess == '22':
        guess.remove ('22')
        print("You got one!")
    if guess == '40':
        guess.remove ('40')
        print("You got one!")
    if guess == '34':
        guess.remove ('34')
        print("You got one!")
    if guess == '58':
        guess.remove ('58')
        print("You got one!")
    if guess == '55':
        guess.remove ('55')
        print("You got one!")
    if guess == '73':
        guess.remove ('73')
        print("You got one!")
    if guess == '68':
        guess.remove ('68')
        print("You got one!")
    # else
    #     print("try again!")
    # if []
    #      break