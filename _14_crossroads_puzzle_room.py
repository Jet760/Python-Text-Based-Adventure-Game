import room


class CrossRoadsRoom(room.Room):

    def room_script(self):
        self.has_been_visited = True
        print("While walking down the path you come to a cross roads.")
        print("There is a sign post with wooden arrows pointing in three directions.")
        print('The first arrow is pointing EAST - it reads "HAZELMAW".')
        input("-press enter to continue-")
        print("")
        print('The second arrow is pointing SOUTH - it reads "FAYLIGHT".')
        input("-press enter to continue-")
        print("")
        print('The third arrow is pointing WEST - it reads "FAIRFORD".')
        input("-press enter to continue-")
        print("")
