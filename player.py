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

    def remove_item_from_backpack(self, item):
        if item is not None:
            self.backpack.remove_item(item)

    def get_item_name(self, position):
        return self.backpack.get_item_name(position)

    def find_item_and_return_name(self, item):
        position = self.find_item_backpack(item)
        return self.get_item_name(position)


