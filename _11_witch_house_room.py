import room


class WitchHouseRoom(room.Room):

    def room_script(self):
        self.has_been_visited = True
        print("You decide to take her up on her offer of tea.")
        print("You open the wooden gate and enter her garden.")
        print("You follow the path up to her cottage.")
        print("There is a little wooden sign picturing a lady riding a broomstick.")
        print('"Kiki\'s Cottage" is written on the sign.')
        input("-press enter to continue-")
        print("")
        print("You push open the door and peer inside.")
        print('"I\'m glad you decide to stay for tea!" calls out Kiki from the kitchen')
        print("You walk through the door and shut it behind you.")
        print("You feel something pressing against your legs.")
        print("You look down to see a black cat!")
        input("-press enter to continue-")
        print("")
        print(f'"That\'s Jiji! Say hello to {self.player.name}, Jiji."')
        print("Jiji inspects you with his eyes for a few seconds")
        print('"Hello" he says curtly, "I\'m Jiji, Kiki\'s cat.')
        print('"You can talk??" you blurt out')
        print('"Of course I can talk, I\'m a witch\'s cat! not just some regular moggy." he huffs')
        input("-press enter to continue-")
        print(f'"Come {self.player.name}, sit down, the tea is ready!" Kiki says, carrying a'
              f' tray over to the dining table.')
        print('You walk over and sit down')
        print('"Careful! The tea is still hot" Kiki says as she hands you a cup')
        print('You gently take the tea from her, saying thank you')
        sip_counter = 0
        ask = True
        while ask:
            print("To talk, please enter the corresponding number")
            print("Please enter 1 to ask Kiki how she became a witch:")
            print("Please enter 2 to ask Kiki what sort of magic she does:")
            print("Please enter 3 to drink your tea:")
            print("Please enter 9 to leave the conversation:")
            instruct = input("> ")
            if instruct == "1":
                print('"How did you become a witch Kiki?" you ask')
                print('"I was born a witch" she replies, "my mother was a witch, so when I turned 13 I left '
                      'home to begin my journey as a witch"')
                print('"Wow so young"')
                input("-press enter to continue-")
                print("")
            elif instruct == "2":
                print('"What sort of witch are you Kiki? What sort of magic do you do?" you ask')
                print('"I started out doing deliveries on my broomstick."')
                print('"Now I tend to my garden and make potions to help the folk that live in this forest."')
                input("-press enter to continue-")
                print("")
            elif instruct == "3":
                print('You take a sip of your tea')
                print('It\'s delicious!')
                sip_counter += 1
                input("-press enter to continue-")
                print("")
            elif instruct == "9":
                print('"Thank you for the chat and the tea, it was lovely!"')
                print('You stand up.')
                print('"Thank you for stopping by! Jiji and I dont get visitors very often do we Jiji?"')
                print('"That\'s probably for the best" Jiji muttered under his breath')
                input("-press enter to continue-")
                print("")
                if sip_counter < 6:
                    print("You realise you haven't finished your tea.")
                    ask2 = True
                    while ask2:
                        print("Do you want to save your tea for later or scull it?")
                        print("Enter 1 for save it:")
                        print("Enter 2 for scull it:")
                        instruct2 = input("> ")
                        if instruct2.lower() == "1":
                            print("You put the tea in your backpack for later.")
                            self.player.add_to_backpack("tea")
                            ask2 = False
                        elif instruct2.lower() == "2":
                            print("You decide to scull the tea before leaving.")
                            ask2 = False
                        elif instruct2.lower() == "i":
                            self.player.check_backpack()
                        else:
                            continue
                ask = False
            elif instruct.lower() == "i":
                self.player.check_backpack()
            else:
                continue
