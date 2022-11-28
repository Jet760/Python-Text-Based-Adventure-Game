import super_death_room


class DeathRoomWrongWay(super_death_room.DeathRoom):

    def room_script(self):
        # TODO:
        print("You continue down the path, when suddenly the ground gives way underneath you.")
        print("You find yourself at the bottom of a deep hole.")
        print("You shout and shout, hoping someone with help you.")
        item = self.player.find_item_backpack("rope")
        if item != False:
            input("-press enter to continue-")
            print("")
            print("You suddenly remember the rope you put in your backpack earlier!")
            print("You create a loop on one end and manage to throw it out of the hole and hook it on a tree.")
            print("You slowly pull yourself out of the hole.")
            print("Once you make it out, you lay on your back and stare up into the canopy of the trees for a minute,"
                  " catching your breath.")
            input("-press enter to continue-")
            print("")
            print("You pick yourself up off the floor.")
            print("You decide to leave the rope in the hole, just incase someone else fell in.")
            self.player.remove_item_from_backpack("rope")
            print("You start walking onwards, hoping you reach this town soon.")
            input("-press enter to continue-")
            print("")
        else:
            input("-press enter to continue-")
            print("Try to climb out but the sides are too steep and you just keep coming crashing back down.")
            print("You scream for hours, but to no avail.")
            print("The sun sets and you start to feel the cold seeping into your bones.")
            print("As you sit at the bottom of the hole, clutching you knees to your chest, you feel yourself falling "
                  "asleep...")
            print("...")
            input("-press enter to continue-")
            print("")
            self.died = True




