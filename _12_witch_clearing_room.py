import room


class WitchClearingRoom(room.Room):
    def __init__(self, name, number, north=None, east=None, south=None, west=None):
        super().__init__(name, number, north, east, south, west)
        self.has_flower = False
        self.gave_flower = False
        self.flower_name = ''

    def room_script(self):
        if self.has_been_visited is False:
            self.has_been_visited = True
            print("You walk down the path for a while until you come to the next clearing.")
            print("You come across a lovely garden surrounded by a low stone wall.")
            input("-press enter to continue-")
            print("")
            print("Suddenly you notice there is a person in the garden! They are bent over some plants.")
            print('"Hi!" you call out')
            print("She stands up with a start.")
            print('"Hello! You surprised me, we don\'t get many visitors this deep in the forest!"')
            input("-press enter to continue-")
            print('')
            ask = True
            while ask:
                print("To talk, please enter the corresponding number")
                print("Please enter 1 to ask her name:")
                print("Please enter 2 to ask why she lives here:")
                print("Please enter 3 to compliment her garden:")
                print("Please enter 4 to ask for directions:")
                position = self.player.find_item_backpack("marigold")
                if position is False:
                    position = self.player.find_item_backpack("yarrow")
                if position:
                    self.has_flower = True
                    self.flower_name = self.player.get_item_name(position)
                    print("Please enter 5 to give her a flower:")
                print("Please enter 9 to leave the conversation:")
                instruct = input("> ")
                if instruct == "1":
                    print('"What is your name?" you ask')
                    print('"My name is Kiki!" she replies enthusiastically, "what\'s yours?"')
                    print(f'"My name is {self.player.name}"')
                    input("-press enter to continue-")
                    print("")
                elif instruct == "2":
                    print('"Why do you live out here, in the middle of the forest?" you ask')
                    print('"I\'m a witch!" she replies, "what are YOU doing in the middle of the forest?"')
                    print('You explain about your car breaking down and told her your journey so far.')
                    print('"Wow that\'s a lot for one day" she says')
                    input("-press enter to continue-")
                    print("")
                elif instruct == "3":
                    print('"Your garden looks so lovely!" you say')
                    print('"Thank you!" she smiles proudly')
                    input("-press enter to continue-")
                    print("")
                elif instruct == "4":
                    print('"Would you be able to direct me to the town?" you ask')
                    print('"You are on the right path! Keep following it and it will take you where you need to go!" '
                          'she replies')
                    input("-press enter to continue-")
                    print("")
                elif instruct == "5":
                    if self.has_flower:
                        print("You remember the flower you picked up earlier and decide to give it to her.")
                        print(f"You rustle around in your backpack and pull out the {self.flower_name} flower.")
                        print(f"You hold the {self.flower_name} out towards her.")
                        print(f'"Would you like this {self.flower_name}?" you sheepishly ask')
                        print('"OMG YES!!" she squeals and takes the flower from you')
                        print('"Thank you so much!!"')
                        input("-press enter to continue-")
                        print("")
                        print('"If you would like, you can come inside my cottage for some tea!" she says, beaming')
                        print('"Just follow this path through the garden EAST and you will find it."')
                        self.player.remove_item_from_backpack(self.flower_name)
                        self.gave_flower = True
                        self.room_east = 11
                        self.update_rooms()
                        input("-press enter to continue-")
                        print("")
                    else:
                        print("You look in your backpack and can't find the flower")
                elif instruct == "9":
                    print('"I better head back inside, it was nice talking to you" she says')
                    print('"Thanks for the chat!" you say as you turn and head back to the path')
                    input("-press enter to continue-")
                    print("")
                    ask = False
                elif instruct.lower() == "i":
                    self.player.check_backpack()
                else:
                    continue

        else:
            print("You step out of the cottage and into Kiki's garden.")
            print("You look around and admire her luscious plants.")
            print("You make your way slowly down the garden path.")
            print("You close the little wooden gate behind you.")
            input("-press enter to continue-")
            print("")
