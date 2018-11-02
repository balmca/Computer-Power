# NOTES: Validates Position of Ship


class Validator:

    def is_valid_position(self, row, col):
        if (row and col >= 5) or (row and col < 0):
            # Displays message when Position outside Board
            print("Ship placed! Warning. At least one position for this ship is invalid.")
        else:
            # Displays message when Position inside Board
            print("Entered valid position.")




