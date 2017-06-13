class Ship:
    ship_types = {'Carrier': 5,
                  'Battleship': 4,
                  'Cruiser': 3,
                  'Submarine': 3,
                  'Destroyer': 2}

    def __init__(self, name, positions, is_vertical=False):
        self.name = name
        self.positions = positions
        self.is_vertical = is_vertical

    def is_sunk(self):
        sunk = True
        for square in self.positions:
            if not square.is_marked():
                sunk = False
        return sunk


re.match("^[a-jA-J][1-9]$|^[a-jA-J][1][0]$", input)
