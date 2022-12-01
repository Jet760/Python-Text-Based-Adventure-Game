import room


class RoyalEndingRoom(room.Room):

    def room_script(self):
        print("You follow Avery out of the clearing and down a path. ")
        print("She turns to you. ")
        print('"Would you like to meet the fairy queen?" she asks. ')
        print('"How can I refuse" you reply. ')
        print('"Excellent!!" she exclaims. ')
        input("-press enter to continue-")
        print("")
        print("You continue down the path until a big beautiful palace comes into view.")
        print("Tucked away in the woods next to a stream, the palace looks like its made of branches and"
              " other natural material from the forest.")
        print("It is as tall as the tops of the trees. ")
        input("-press enter to continue-")
        print("")
        print("Avery beckons you to stand beside her at the entrance. ")
        print('"The queen has invited you to her banquet" she whispers in your ear. ')
        print("The doors are flung open to reveal a large wooden table covered in food.")
        input("-press enter to continue-")
        print("")
        print("Avery leads you to a seat and you sit down.")
        print("Once everyone is seated the fairy queen entered.")
        print("She has beautiful shimmering, iridescent wings and a long white dress that touches the ground.")
        print('She takes a seat and everyone around the table begins eating.')
        print('She leans over to you and thanks you for attending.')
        input("-press enter to continue-")
        print("")
        print("You spend the evening eating and having fun.")
        print("Once the banquet is over the queen offers you her personal carriage to take you home.")
        print("You gladly except, you are happy to not have to do anymore walking.")
        print("You bid farewell to the queen and Avery takes you to where the carriage is waiting.")
        input("-press enter to continue-")
        print("")
        print('"The is the driver, Kurt" Avery says, the frog sitting on the front of the carriage '
              'tips his hat to you. ')
        print('"Eggy and Dot will be pulling the carriage tonight" Avery says as she opens the door, the two deer in'
              ' harness nod to you. ')
        print("You climb inside the carriage.")
        print("You say goodbye to Avery and set off home.")
        input("-press enter to continue-")
        print("")
        print("Wondering if you imagined the whole experience the day before, ")
        print("you wake up the next day and call a tow truck to go pick up your car and take it to the mechanics.")

    def room_actions(self):
        return "ending"
