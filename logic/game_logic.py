class Game_Logic:

    def __init__(self, logic_wrapper):
        self.logic_wrapper = logic_wrapper

    def create_game(self, game):
        return self.logic_wrapper.create_game(game)

    def get_all_games(self):
        return self.logic_wrapper.get_all_games()