# NOTES: Run File
# Will import from Class: Game


from Game import Game


user_name = input("Enter your name: ")  # User enter Player Name
# Instructions for Player
print("The program will ask the user to place a ship in a 5 x 5 sea grid.")
print("The ship can lie either horizontally(0-4) or vertically(0-4).")
print("Every ship has size equivalent to 3 position.")
print("\n")
print("Commands:")
print("To place ship type: place <v/h>,row,col.")
print("To show ships type: show ships.")
print("To exit battleships: exit battleships")
print("\n")
# Access Game Class
game = Game()
game.get_player_name(user_name)


