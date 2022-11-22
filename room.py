class Room:
    """
            sfsdfsf
            :param name: room name
            :param number: room number
            :param north: room number
            :param east: room number
            :param south: room number
            :param west: room number
            """

    def __init__(self, player, name, number, north=None, east=None, south=None, west=None):
        """
        sfsdfsf
        :param name: room name
        :param number: room number
        :param north: room number
        :param east: room number
        :param south: room number
        :param west: room number
        """
        self.room_name = name
        self.room_number = number
        self.has_been_visited = False
        self.room_north = north
        self.room_east = east
        self.room_south = south
        self.room_west = west
        self.room_list, self.direction_list = self.room_choices()
        self.item = None
        self.player = player

    def room_script(self):
        print("room list")

    def room_choices(self):
        room_list = []
        direction_list = []
        if self.room_north is not None:
            room_list.append(self.room_north)
            direction_list.append("N")

        if self.room_east is not None:
            room_list.append(self.room_east)
            direction_list.append("E")

        if self.room_south is not None:
            room_list.append(self.room_south)
            direction_list.append("S")

        if self.room_west is not None:
            room_list.append(self.room_west)
            direction_list.append("W")

        return room_list, direction_list

    def choose_next_room(self):
        result = ""
        loop = True
        while loop:
            print("________________________________________________________________")
            print(" Please enter one of the listed directions to enter the next area ")
            print("________________________________________________________________")
            print(self.direction_list)

            choice = input("> ")

            if choice.lower() == "n":
                result = self.room_north
            elif choice.lower() == "e":
                result = self.room_east
            elif choice.lower() == "s":
                result = self.room_south
            elif choice.lower() == "w":
                result = self.room_west
            elif choice.lower() == "i":
                self.player.check_backpack()
            else:
                print("Incorrect input, please try again")
                continue

            if result is not None:
                loop = False
            else:
                print("Incorrect input, please try again")

        return result

    def room_actions(self):
        return None


