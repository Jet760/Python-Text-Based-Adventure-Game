import super_death_room


class DeathRoomPit(super_death_room.DeathRoom):

    def room_script(self):
        print("You continue down the path, when suddenly the ground gives way underneath you.")
        print("You find yourself at the bottom of a deep hole.")
        print("You shout and shout, hoping someone with help you.")
        item = self.player.find_item_backpack("rope")
        if item != False:
            input("-press enter to continue-")
            print("You suddenly remember the rope you put in your backpack earlier!")
            print("You create a loop on one end and manage to throw it out of the hole and hook it on a tree.")
            print("You .")

        self.died = True




