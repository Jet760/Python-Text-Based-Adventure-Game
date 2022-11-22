class Player:

    def __init__(self, backpack):
        self.name = self.ask_player_name()
        self.backpack = backpack

    def ask_player_name(self):
        name = input("Please enter your name: ")
        return name

    def add_to_backpack(self, item):
        self.backpack.add(item)

    def check_backpack(self):
        self.backpack.list()

    def find_item_backpack(self, item):
        return self.backpack.in_backpack(item)

