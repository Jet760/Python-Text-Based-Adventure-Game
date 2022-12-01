import super_death_room


class DeathRoomWrongWay(super_death_room.DeathRoom):

    def room_script(self):
        print("You turn and walk down the path.")
        print("You walk.")
        input("-press enter to continue-")
        print("")
        print("And walk.")
        input("-press enter to continue-")
        print("")
        print("And walk.")
        input("-press enter to continue-")
        print("")
        print("And walk.")
        print("The sun is starting to get lower in the sky.")
        print("You have been walking for hours and are starting to feel pretty exhausted.")
        input("-press enter to continue-")
        print("")
        print("You decide to sit down against a tree and have a quick rest.")
        item = self.player.find_item_and_return_name("lemonade")
        if item != "lemonade":
            item = self.player.find_item_and_return_name("tea")
            if item != "tea":
                item = False
        if item is not False:
            input("-press enter to continue-")
            print("")
            print(f"You grab your backpack and take out the {item} you saved from earlier.")
            print(f"While drinking the {item} you decide to go walk back the way you came and try another path.")
            print("After resting you climb to your feet and walk back.")
            input("-press enter to continue-")
            print("")
            self.player.remove_item_from_backpack(item)
        else:
            input("-press enter to continue-")
            print("You sit for a while and rest.")
            print("Once you feel ready to continue you get up and continue walking down the path.")
            input("-press enter to continue-")
            print("")
            print("You just keep walking, hoping you will soon reach the town.")
            print("The sun sets and you start to feel the cold seeping into your bones.")
            print("You sit at the bottom of a tree to take another rest, clutching you knees to your chest, "
                  "you feel yourself falling asleep...")
            print("...")
            input("-press enter to continue-")
            print("")
            self.died = True




