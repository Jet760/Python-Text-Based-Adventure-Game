class Deer:

    def __init__(self):
        self.has_been_saved = False
        self.inventory = []

    def ask_to_be_saved(self):
        print("something")

    def add_item_to_inventory(self, item):
        self.inventory.append(item)
