# NOTES: Position stores co-ordinates of Ship


class Position:

    def horizontal_position(self, row, col):
        # Increase starting position for Ship (3)
        horizontal = []
        hor_pos = (row, col), (row, col + 1), (row, col + 2)
        horizontal.append(hor_pos)
        return horizontal

    def vertical_position(self, row, col):
        # Increase starting position for Ship (3)
        vertical = []
        ver_pos = (row, col), (row + 1, col), (row + 2, col)
        vertical.append(ver_pos)
        return vertical
