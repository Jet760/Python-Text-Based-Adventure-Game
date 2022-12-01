import room


class HumanEndingRoom(room.Room):

    def room_script(self):
        print("You follow Dana down a path and eventually come to a human town. ")
        print("She points you in the direction of the mechanic. ")
        print("You meet the mechanic, and explain your situation to her. ")
        print("She agrees to come take a look at your car. ")
        print("You ride with her to your broken car.")
        input("-press enter to continue-")
        print("")
        print("She fixes up your car and sends you on your way.")
        print('As you are driving home, you try to convince yourself that the whole thing wasn\'t a dream')
        input("-press enter to continue-")
        print("")

    def room_actions(self):
        return "ending"
