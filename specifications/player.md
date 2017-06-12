# class description
    Holds players attributes


# instance attributes
- `name`
    - data: str
    - description: players name.
- `player_ocean`
    - data: Ocean class object
    - description: board with players ships.
- `enemy_ocean`
    - data: Ocean class object
    - description: enemy board with hits and misses.


# instance methods
- `choose_initial_ships_position(self)`
    - Takes ships positions from user.
    - returns: dictionary with ships names as keys and tupples of given_positions as values
- `check_if_position_are_valid(self, given_position)`
    - Checks if ships don't overlay each other and don't hang off the edge.
    - returns: bool
- `choose_shoot_cords(self)`
    - Takes coordinates for atack from user.
    - returns: tuple with two integers
- `win_or_lose(self)`
    - Checks if there is any part of ship left
    - returns: bool
