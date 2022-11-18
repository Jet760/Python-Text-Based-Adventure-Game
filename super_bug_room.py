import room


class BugRoom(room.Room):

    def room_script(self):
        self.has_been_visited = True
        print("You come across an old stone wall blocking the path. ")
        print("The wall is overgrown with ivy and lichen. ")
        print("The path leads to a wooden gate in the wall. ")
        print("You pull back the ivy and try push the gate open. ")
        print("It seems to be locked.")
        print("You look to the side and notice three coloured stones jutting out of the wall:")
        print("The stones are coloured Green, Blue, Red")
        print("To open the gate you will need to press them in the correct order.")
        try_counter = 0
        ask = True
        while ask:
            print("Please enter the sequence of colours you want to try: ")
            print("Type G for Green:")
            print("Type B for Blue:")
            print("Type R for Red:")
            print("Enter five letters in sequence, for example:")
            print("GRGBB")
            instruct = input("> ")
            if instruct.lower() == "rbgbr":
                print("You hear a click.")
                print("The gate swings open.")
                print("You walk through and keep following the path though the forrest.")
                ask = False
            else:
                print("You push the rocks.")
                print("...")
                print("Nothing happens.")
                print("Try again.")
                print("")
                try_counter += 1
                if try_counter == 3:
                    ask2 = True
                    while ask2:
                        print("Would you a hint?")
                        print("Please enter Y for yes and N for no:")
                        instruct2 = input("> ")
                        if instruct2.lower() == "y":
                            print("Have a squiz under the log ;)")
                            print("...")
                            print("You walk back to the clearing where you saw the log.")
                            print("You spot the large rotting log off at the edge of the clearing.")
                            ask3 = True
                            while ask3:
                                print("Do you want to roll the log?")
                                print("Please enter Y for yes and N for no:")
                                instruct3 = input("> ")
                                if instruct3.lower() == "y":
                                    print("You roll the log over to reveal three brightly coloured bugs.")
                                    print("You watch the bugs for a little while and notice they flash in a pattern.")
                                    print("Red, Blue, Green, Blue, Red.")
                                    print("...")
                                    print("Red, Blue, Green, Blue, Red.")
                                    print("...")
                                    print("Red, Blue, Green, Blue, Red.")
                                    print("You walk back to the stone wall ready to try again.")
                                    ask3 = False
                                elif instruct3.lower() == "n":
                                    print("You walk back to the stone wall without looking under the log.")
                                    ask3 = False
                                else:
                                    continue
                            try_counter = 0
                            ask2 = False
                        elif instruct2.lower() == "n":
                            try_counter = 0
                            ask2 = False
                        else:
                            continue
                continue




