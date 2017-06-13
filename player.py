class Player:
    pass

    def __init__(self, name, player_ocean, enemy_ocean):
        self.name = name
        self.player_ocean = player_ocean
        self.enemy_ocean = enemy_ocean

    def choose_initial_ships_position(self):
        """
        Takes ships positions from user.
        returns
        ---------
        dictionary with ships names as keys and tupples of given_position
        as values
        """

        given_position = {}
        

    def check_if_position_are_valid(self, given_position):
        pass

    def choose_shoot_cords(self):
        pass

    def is_win(self):
        pass
