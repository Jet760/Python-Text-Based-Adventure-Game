import room


class MushroomRoom(room.Room):
    def __init__(self, name, number, north=None, east=None, south=None, west=None):
        super().__init__(name, number, north, east, south, west)
        self.picked_mushroom = False

    def room_script(self):
        self.has_been_visited = True
        print("As you walk down the path you notice different three clumps of mushrooms ")
        print("    growing on the side of the path.")
        print("You crouch down to take a better look at them.")
        print("...")
        print("The first one is some Scarlet Elf Cups ")
        print("They are vivid scarlet and their mushroom cap is cup shaped.")
        print("...")
        print("The second is some Fly Agaric ")
        print("They are the classic toad stool shape with white stalk, and red cap that is spotted with white dots.")
        print("...")
        print("The third is some Common Puffball ")
        print("Their cap is a round bulb coming from the end of the stalk, the")
        print("    surface of the mushroom is cream in colour and is covered in tiny pyramid-shaped pearls")
        ask = True
        while ask:
            print("Would you like to pick one of the mushrooms?")
            print("Please enter 1 if you would like to pick a Scarlet Elf Cup:")
            print("Please enter 2 if you would like to pick a Fly Agaric:")
            print("Please enter 3 if you would like to pick a Common Puffball:")
            print("Please enter 4 if you don't want to pick a mushroom:")
            instruct = input("> ")
            if instruct == "1":
                print("You pick a Scarlet Elf Cup and put it in your backpack.")
                self.picked_mushroom = "scarlet_elf_cup"
                ask = False
            elif instruct == "2":
                print("You pick a Fly Agaric and put it in your backpack.")
                self.picked_mushroom = "fly_agaric"
                ask = False
            elif instruct == "3":
                print("You pick a Common Puffball and put it in your backpack.")
                self.picked_mushroom = "common_puffball"
                ask = False
            elif instruct == "4":
                print("You don't pick up any of the mushrooms.")
                ask = False
            elif instruct.lower() == "i":
                self.player.check_backpack()
            else:
                continue
        print("You stand up and keep walking down the path.")

    def room_actions(self):
        if self.picked_mushroom is not False:
            self.item = self.picked_mushroom
            return self.item
        else:
            return None



