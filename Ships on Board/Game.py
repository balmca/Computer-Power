# NOTES: Game responds to Player - also Start, Loop and Exit
# Will import from ALL Class: Board, Position, Validator, Player


from Board import Board
from Position import Position
from Validator import Validator
from Player import Player


class Game:

    col = 0     # Beginning Value for Col
    row = 0     # Beginning Value for Row

    # Get Name from Player
    def get_player_name(self, user_name):
        player = Player()
        player.player_name(user_name)

        # Begin Loop
        while True:
            user_input = input("enter a command:").split(" ")
            print("\n")

            # Respond to Player
            if user_input[0] == 'place':
                command = user_input[0]
                user_ship = user_input[1].split(",")
                orientation = user_ship[0]
                r = user_ship[1]
                row = int(r)
                c = user_ship[2]
                col = int(c)

                place = Validator()
                place.is_valid_position(row, col)

                b1 = Board()
                b1.place_ship(orientation, row, col)

                if orientation == 'h':
                    p1 = Position()
                    p1.horizontal_position(row, col)

                elif orientation == 'v':
                    p2 = Position()
                    p2.vertical_position(row, col)
            # Show Ship
            elif user_input[0] == 'show':
                b2 = Board()
                b2.show_ships(row, col)
            # Exit Loop
            elif user_input[0] == 'exit':
                print("\nSee you later.\n")
                break
            else:
                # Provide this message when entered value is not in the choices.
                print("\nI don't understand that choice, please try again.\n")






