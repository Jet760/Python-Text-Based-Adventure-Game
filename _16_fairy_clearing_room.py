import room


class FairyClearingRoom(room.Room):
    def __init__(self, name, number, north=None, east=None, south=None, west=None):
        super().__init__(name, number, north, east, south, west)
        self.ending = 0
        self.loop = True

    def room_script(self):
        print("As the sun is starting to get low in the sky you come across another clearing in the trees.")
        print("You spot a tree stump and sit for a rest.")
        input("-press enter to continue-")
        print("")
        print("While sitting on the stump you notice three little glowing people watching you from the forest.")
        print("You decide not to call out this time just in case you scare them.")
        print("Eventually they flutter over to you.")
        print('"Hi" says the green one.')
        print('"Hello" you respond, surprised.')
        input("-press enter to continue-")
        print("")
        print('Now that you can see them up close you can see they are little fairies!.')
        print('One has blue glowing wings and a blue dress.')
        print('Another has green glowing wings and a green dress.')
        print('The last has red glowing wings and a red dress.')
        input("-press enter to continue-")
        print('')
        while self.loop:
            print("To talk, please enter the corresponding number")
            print("Please enter 1 to ask their name:")
            print("Please enter 2 to ask about them:")
            print("Please enter 3 to compliment their wings:")
            print("Please enter 4 to ask for directions:")
            instruct = input("> ")
            if instruct == "1":
                print('"What is your name?" you ask them')
                print('"My name is Dana" says the blue fairy')
                print('"My name is Avery" says the green fairy')
                print('"My name is Twisty" says the Red fairy')
                print(f'"And your name is?"')
                print(f'"{self.player.name}" you reply')
                input("-press enter to continue-")
                print("")
            elif instruct == "2":
                print('"So are you fairies?" you ask')
                print('"Yes!" the green fairies replies, "Have you never met a fairy before??"')
                print('"No I haven\'t" you reply')
                print('"Do you live in the woods?" you ask')
                print('"We live in the town FAYLIGHT" the red fairy responds')
                input("-press enter to continue-")
                print("")
            elif instruct == "3":
                print('"Your wings are so beautiful!" you say')
                print('"Thank you!" says the green fairy, the other two just blush')
                input("-press enter to continue-")
                print("")
            elif instruct == "4":
                print('"Would you be able to direct me to the town?" you ask')
                print('"My car broke down and I need to find a mechanic or get it towed"')
                print('"We can help you" the blue fairy replies')
                print('"But we need something in return" says the green fairy')
                print('"Do you have any mushrooms with you?" asks the red fairy, her eyes lighting up')
                input("-press enter to continue-")
                print("")
                mushroom = self.player.find_item_and_return_name("scarlet_elf_cup")
                if mushroom == "scarlet_elf_cup":
                    self.ending = 1
                    print("You reach into your backpack and pull out the scarlet elf cup that you collected "
                          "earlier.")
                    print("The green fairy reaches out and takes it from you.")
                    self.player.remove_item_from_backpack("scarlet_elf_cup")
                    print('"Follow me!".')
                    self.room_north = None
                    self.room_south = 18
                    self.update_rooms()
                    self.loop = False
                else:
                    mushroom = self.player.find_item_and_return_name("fly_agaric")
                    if mushroom == "fly_agaric":
                        self.ending = 2
                        print("You reach into your backpack and pull out the fly agaric that you collected "
                              "earlier.")
                        print("The red fairy flutters up to you and takes it from you.")
                        self.player.remove_item_from_backpack("fly_agaric")
                        print('"Follow me!!".')
                        self.room_north = None
                        self.room_west = 19
                        self.update_rooms()
                        self.loop = False
                    else:
                        mushroom = self.player.find_item_and_return_name("common_puffball")
                        if mushroom == "common_puffball":
                            self.ending = 3
                            print("You reach into your backpack and pull out the common puffball that you collected "
                                  "earlier.")
                            print("The blue fairy holds her hand out and you give her the mushroom.")
                            self.player.remove_item_from_backpack("common_puffball")
                            print('"Follow me".')
                            self.room_east = 17
                            self.room_north = None
                            self.update_rooms()
                            self.loop = False
                        else:
                            print("You shake your head.")
                            print('"I don\'t have a mushroom" you tell them')
                            print('"We will wait" the blue fairy says')
                            print('They all sit and get comfortable.')
                            print('You stand up with a sigh.')
                            print('You begin the walk back to the place that had the mushrooms.')
                            self.room_north = 20
                            self.update_rooms()
                            self.loop = False
            elif instruct.lower() == "i":
                self.player.check_backpack()
            else:
                continue
        self.loop = True
