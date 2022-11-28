import room


class StartingRoom(room.Room):

    def room_script(self):
        #self.has_been_visited = True
        print("You are driving home through a forest when your car dies.")
        print("You pull over onto the shoulder of the road.")
        input("-press enter to continue-")
        print("")
        print("You check your phone, no service.")
        print("You get out of your car and look around.")
        print("You spot a wooden sign.")
        print("You walk over to take a closer look.")
        input("-press enter to continue-")
        print("")
        print('The sign reads "FAYLIGHT".')
        print("You can now see the sign is pointing down a path.")
        print("You check your watch.")
        print("It reads 3pm.")
        print("You decide to see if you can walk to the town to get some help.")
        input("-press enter to continue-")
        print("")
        print(self.room_south)
        self.update_rooms()
