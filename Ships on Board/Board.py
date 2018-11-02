# NOTES: Board stores board size and valid position of the ship within the board
# Will import from Class: Position


from Position import Position


class Board:

    ship_list = []  # List of Ship Positions
    board_size = 5  # Size of Board (5x5 grid)

    # Place Ship on Board
    def place_ship(self, orientation, row, col):
        print("Entered coordinates: row is", row,",", "col is", col)

        if orientation == 'v':
            shipv = Position.vertical_position(orientation, row, col)
            self.row = row
            self.col = col
            self.ship_list.append(shipv)
            print("Entered position: vertical")

        else:
            shiph = Position.horizontal_position(orientation, row, col)
            self.row = row
            self.col = col
            self.ship_list.append(shiph)
            print("Entered position: horizontal")

    # Show Ships on Board
    def show_ships(self, col, row):
        print("Ships at sea:")
        print("Ship at", self.ship_list)
        if (row or col) > self.board_size:
            print("Warning! At least one position for this ship is invalid.")
        else:
            print("Valid")














