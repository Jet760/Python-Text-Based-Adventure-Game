import super_death_room


class DeathRoomWaterfall(super_death_room.DeathRoom):

    def room_script(self):
        print("As you walk on, you come across a bubbling stream running parallel to the path.")
        print("You enjoy the lovely calming gurgles and ripples.")
        print("Soon you start to hear a distant roar.")
        print("The stream next to you widens and the path you are on becomes more rocky.")
        print("Eventually the path leads you to the edge of a cliff.")
        input("-press enter to continue-")
        print("")
        print("The stream rushes besides you and creates a beautiful waterfall off the edge of the cliff.")
        print("You peer over the edge and see the waterfall splash down into a rocky river bed.")
        input("-press enter to continue-")
        print("")
        print("You turn to head back to the path...")
        print("when suddenly you feel your foot slide out from under you on the slippery rocks.")
        print("You scramble to gain control of your footing.")
        print("...")
        print("You try in vain, you can already feel yourself falling through the air, ")
        print("    mist from the waterfall landing on your face, and then...")
        print("nothing")
        print("")
        self.died = True




