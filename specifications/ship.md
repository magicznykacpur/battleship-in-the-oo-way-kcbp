# class description
    Holds data needed for proper ship description and methods for management.


# class atrributes
- `ships_types`
    - data: dict
    - description: keys with ships names and values with corresponding lenghts.
    Used for length instance attribute creation.


# instance attributes
- `name`
    - data: str
    - description: one of 5 possible ship names.
- `positions`
    - data: tuple of Square objects
    - description: carries all squares occupied by ship.
- `length`
    - data: int
    - description: indicates how many squares objects ship occupied.
- `is_vertical`
    - data: bool
    - description: indicates ship direction. True if vertical, False if horizontal.


# instance methods
- `__init__(self, name, positions)`
    - Creates Ship object with name and position.
- `is_sunk(self)`
    - Checks if ship is sunk or not.
    - returns: bool
