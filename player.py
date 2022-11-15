class Player:

    def __init__(self):
        self.name = self.ask_player_name()
        self.backpack = None

    def ask_player_name(self):
        name = input("Please enter your name: ")
        return name

    def input_backpack(self, backpack):
        self.backpack = backpack

    def add_to_backpack(self, item):
        pass
