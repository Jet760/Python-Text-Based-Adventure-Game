import room


class FaeEncounterRoom(room.Room):

    def room_script(self):
        self.has_been_visited = True
        print("You are continuing down the path when you spot something glowing ahead.")
        print("You quicken your pace.")
        print("The glowing appears to also quicken.")
        print("You walk even faster to try and catch a proper glimpse.")
        input("-press enter to continue-")
        print("")
        print("You manage to catch up slightly.")
        print('The glowing thing seems to be a tiny person!')
        print("You admire their delicate glowing wings.")
        print('"Hello" you call out.')
        input("-press enter to continue-")
        print("")
        print("The little person squeaks and quickly flutters away into the woods.")
        print("You feel disappointed that you scared them off.")
        print('You continue to trudge along, starting to get rather annoyed that you hadn\'t reached the town yet.')
        input("-press enter to continue-")
        print("")
