import room


class DeerRoom(room.Room):
    def __init__(self, name, number, north=None, east=None, south=None, west=None):
        super().__init__(name, number, north, east, south, west)
        self.took_rope = False

    def room_script(self):
        self.has_been_visited = True
        print("You walk down the path for a while until you come to the next clearing.")
        print('"Hey! You there!"')
        print('"Could you please help me!!"')
        print("To your surprise, you turn to see a deer standing next to a tree.")
        print("You walk closer and notice that the deer's back legs are ")
        print("    completely tangled in a rope attached to the tree.")
        print('"Could you please help untangle me?"')
        ask = True
        while ask:
            print("Would you like to help the deer? ")
            print("Please enter Y for yes and N for no:")
            instruct = input("> ")
            if instruct.lower() == "y":
                print("You walk over to the deer and gently free him from the rope.")
                print('"Thank you so much! I have been stuck here for hours hoping someone would find me."')
                print("You tell the deer it's no worries and put the rope in your backpack ")
                print("    so it can't trap anyone else.")
                print("You turn and walk down the path, waving goodbye to the deer.")
                self.took_rope = True
                ask = False
            elif instruct.lower() == "n":
                print("You apologise to the deer and explain you are in a hurry.")
                print("You quickly turn away and scurry on down the path.")
                print("You hear the deer calling after you but you ignore it.")
                ask = False
            elif instruct.lower() == "i":
                self.player.check_backpack()
            else:
                continue

    def room_actions(self):
        if self.took_rope:
            self.item = "rope"
            return self.item
        else:
            return None



