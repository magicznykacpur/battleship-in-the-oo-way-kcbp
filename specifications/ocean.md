# class description
    contains all ships and game board and handles output


# attributes
- `ships`
    - data: list of Ship objects
    - description: holds all ships to append them to the board.
- `board`
    - data: list of lists
    - description: current board state.


# instance methods
- `__init__(self)`
    - Creates object with empty list as an atrribute.
- `__str__(self)`
    - Used for printing current board.
- `add_ship(self, ship)`
    - Inserts Ship object on the board.
- `insert_shoot(self, cords)`
    - Interts shoot mark ('X', 'O') on given coordinates.
