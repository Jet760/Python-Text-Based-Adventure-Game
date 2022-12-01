import room


class FlowerRoom(room.Room):
    def __init__(self, name, number, flower, north=None, east=None, south=None, west=None):
        super().__init__(name, number, north, east, south, west)
        self.flower = flower

    def room_script(self):
        self.has_been_visited = True
        print("Walking down the path you notice the trees thinning out. ")
        print(f"Soon on either side of you are small meadows of flowering {self.flower}.")
        if self.flower == "marigold":
            print("You stop to admire the beautiful, open, orange flowers as they soak up the sun")
        else:
            print("You stop to admire the beautiful clusters of little yellow flowers, stretching up to the sky.")
        input("-press enter to continue-")
        print("")
        ask = True
        while ask:
            print("Would you like to pick a flower?")
            print("Please enter Y for yes and N for no:")
            instruct = input("> ")
            if instruct.lower() == "y":
                print(f"You bend over a pick a few stalks of {self.flower}.")
                if self.flower == "marigold":
                    print("You give the flowers a quick sniff.")
                    print("The marigold has a musky smell, like wet hay or straw")
                else:
                    print("You bring the flowers to your nose.")
                    print("The yarrow smell reminds you of fresh pine needles.")
                print("You carefully place the flowers in your backpack.")
                input("-press enter to continue-")
                print("")
                ask = False
            elif instruct.lower() == "n":
                ask = False
            elif instruct.lower() == "i":
                self.player.check_backpack()
            else:
                continue
            print("You take one last look around at the flowers as you follow the path onwards,")
            print("    back into the thick of the forest.")
            input("-press enter to continue-")
            print("")

    def room_actions(self):
        return self.flower


