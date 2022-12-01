import room


class RaveEndingRoom(room.Room):

    def room_script(self):
        print("Twisty grabs your hand and leads you down a path into the forest. ")
        print("She brings you to a big thicket. ")
        print("There is a toad standing outside a tunnel into the thicket. ")
        print("Twisty gives him a wave as she leads you through the entrance. ")
        print("The toad gives both of you a nod. ")
        input("-press enter to continue-")
        print("")
        print("You soon emerge into the middle of the thicket.")
        print("There is music blaring, flashing lights and a pixie DJ.")
        print('"Surely you will stay and party with us for a while?" Twisty says with a squeal')
        print('The rave seems like fun, there are already heaps of creatures on the dance-floor, so you agree')
        input("-press enter to continue-")
        print("")
        print('You have a great night partying with Twisty')
        print('As it is reaching the early hours of the morning, Twisty calls you a fairy Uber')
        print("You wake up the next day and call a tow truck to go pick up your car and take it to the mechanics.")
        input("-press enter to continue-")
        print("")

    def room_actions(self):
        return "ending"
