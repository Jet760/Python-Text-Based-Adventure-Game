class Player():

    def __init__(self):
        self.name = ask_player_name()

    def ask_player_name(self):
        name = input("Please enter your name: ")
        return name
