import room


class BugRoom(room.Room):

    def roll_log(self):
        ask = True
        while ask:
            print("Do you want to roll the log?")
            print("Please enter Y for yes and N for no:")
            instruct = input("> ")
            if instruct.lower() == "y":
                print("You roll the log over to reveal three brightly coloured bugs.")
                print("You watch the bugs for a little while and notice they flash in a pattern.")
                print("Red, Blue, Green, Blue, Red.")
                print("...")
                print("Red, Blue, Green, Blue, Red.")
                print("...")
                print("Red, Blue, Green, Blue, Red.")
                ask = False
            elif instruct.lower() == "n":
                ask = False
            else:
                continue

    def room_script(self):
        if self.has_been_visited is False:
            print("You enter a clearing and look around.")
            print("You spot a large rotting log off at the edge of the clearing.")
            self.roll_log()
            print("You roll the log back over and continue your journey for help.")

        else:
            print("You walk back to the clearing with the log.")
            print("You spot the large rotting log off at the edge of the clearing.")
            print("You roll the log over to reveal three brightly coloured bugs.")
            print("You watch the bugs for a little while and notice they flash in a pattern.")
            print("Red, Blue, Green, Blue, Red.")
            print("...")
            print("Red, Blue, Green, Blue, Red.")
            print("...")
            print("Red, Blue, Green, Blue, Red.")

    def choose_next_room(self):
        print(self.has_been_visited)
        if not self.has_been_visited:
            self.has_been_visited = True
            result = super().choose_next_room()
            print(result)
            return result

        else:
            print("add link plz")
            # TODO
            # ADD IN LINK TO THE PUZZLE ROOM




