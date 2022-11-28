import room


class FoxRoom(room.Room):
    def __init__(self, name, number, north=None, east=None, south=None, west=None):
        super().__init__(name, number, north, east, south, west)
        self.bought_drink = False

    def room_script(self):
        self.has_been_visited = True
        print("You walk down the path for a while until you come to the next clearing.")
        print('"Hey! You there!"')
        print('"Would you like to buy some lemonade?"')
        input("-press enter to continue-")
        print("")
        print("To your surprise, you turn to see a fox sitting at a lemonade stand.")
        print('"Well? What\'s it gonna be?"')
        print("You brought your wallet with you from the car and have some coins.")
        ask = True
        while ask:
            print("Would you like to buy the lemonade? ")
            print("Please enter Y for yes and N for no:")
            instruct = input("> ")
            if instruct.lower() == "y":
                print("You walk over to the fox and hand him a handful of coins.")
                print('"Thanks! I hope you enjoy it!"')
                print("The fox hands you a cold lemonade.")
                ask2 = True
                while ask2:
                    print("Would you like to drink it now or put it in your backpack to save for later?")
                    print("Please enter 1 for drink it now and 2 for put it in your backpack:")
                    instruct2 = input("> ")
                    if instruct2.lower() == "1":
                        print("You sip on the lemonade.")
                        print("It tastes really good!.")
                        input("-press enter to continue-")
                        print("")
                        ask2 = False
                    elif instruct2.lower() == "2":
                        self.bought_drink = True
                        ask2 = False
                    elif instruct2.lower() == "i":
                        self.player.check_backpack()
                    else:
                        continue
                print("You thank the fox.")
                print("You feel refreshed and have renewed strength to complete your journey.")
                input("-press enter to continue-")
                print("")
                ask = False
            elif instruct.lower() == "n":
                print("You tell the fox no thank you.")
                input("-press enter to continue-")
                print("")
                ask = False
            elif instruct.lower() == "i":
                self.player.check_backpack()
            else:
                continue
        print("You turn and continue walking down the path")

    def room_actions(self):
        if self.bought_drink:
            self.item = "lemonade"
            return self.item
        else:
            return None



