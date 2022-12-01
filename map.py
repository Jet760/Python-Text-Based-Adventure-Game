class Map:
    def __init__(self):
        self.room0 = [" START"]
        self.room1 = ["??????"]
        self.room2 = ["??????"]
        self.room3 = ["??????"]
        self.room4 = ["??????"]
        self.room5 = ["??????"]
        self.room6 = ["??????"]
        self.room7 = ["??????"]
        self.room8 = ["??????"]
        self.room9 = ["??????"]
        self.room10 = ["??????"]
        self.room11 = ["??????"]
        self.room12 = ["??????"]
        self.room13 = ["??????"]
        self.room14 = ["??????"]
        self.room15 = ["??????"]
        self.room16 = ["??????"]
        self.room17 = ["??????"]
        self.room18 = ["??????"]
        self.room19 = ["??????"]

        self.blank = ["------"]

        self.row0 = []
        self.row1 = []
        self.row2 = []
        self.row3 = []
        self.row4 = []
        self.row5 = []
        self.row6 = []
        self.row7 = []
        self.row8 = []

        self.start()

    def start(self):
        self.room0 = [" START"]
        self.room1 = ["??????"]
        self.room2 = ["??????"]
        self.room3 = ["??????"]
        self.room4 = ["??????"]
        self.room5 = ["??????"]
        self.room6 = ["??????"]
        self.room7 = ["??????"]
        self.room8 = ["??????"]
        self.room9 = ["??????"]
        self.room10 = ["??????"]
        self.room11 = ["??????"]
        self.room12 = ["??????"]
        self.room13 = ["??????"]
        self.room14 = ["??????"]
        self.room15 = ["??????"]
        self.room16 = ["??????"]
        self.room17 = ["??????"]
        self.room18 = ["??????"]
        self.room19 = ["??????"]
        self.row0 = [self.room0, self.blank, self.blank, self.blank]
        self.row1 = [self.room1, self.room2, self.room7, self.blank]
        self.row2 = [self.room3, self.room4, self.room5, self.blank]
        self.row3 = [self.room10, self.room6, self.room8, self.blank]
        self.row4 = [self.blank, self.room9, self.room12, self.room11]
        self.row5 = [self.blank, self.blank, self.room13, self.blank]
        self.row6 = [self.blank, self.room15, self.room14, self.room15]
        self.row7 = [self.blank, self.room17, self.room16, self.room18]
        self.row8 = [self.blank, self.blank, self.room19, self.blank]

        self.write_to_file()

    def check_off_room(self, room_number):
        if room_number == 0:
            self.room0[0] = " START"
        elif room_number == 1:
            self.room1[0] = " BUG  "
        elif room_number == 2:
            self.room2[0] = " FOX  "
        elif room_number == 3:
            self.room3[0] = " DEER "
        elif room_number == 4:
            self.room4[0] = "MUSHRM"
        elif room_number == 5:
            self.room5[0] = "BUGPZM"
        elif room_number == 6:
            self.room6[0] = "BUGPZY"
        elif room_number == 7:
            self.room7[0] = " WFALL"
        elif room_number == 8:
            self.room8[0] = "MRIGLD"
        elif room_number == 9:
            self.room9[0] = "YARROW"
        elif room_number == 10:
            self.room10[0] = " PIT  "
        elif room_number == 11:
            self.room11[0] = "WH HSE"
        elif room_number == 12:
            self.room12[0] = " WITCH"
        elif room_number == 13:
            self.room13[0] = "FAE EN"
        elif room_number == 14:
            self.room14[0] = "XRD PZ"
        elif room_number == 15:
            self.room15[0] = "WR WAY"
        elif room_number == 16:
            self.room16[0] = " FAIRY"
        elif room_number == 17:
            self.room17[0] = "HMNEND"
        elif room_number == 18:
            self.room18[0] = "RYLEND"
        elif room_number == 19:
            self.room19[0] = "RVEEND"

        self.write_to_file()

    def print_map(self):
        print("")
        print("You pull out your map")
        print(self.row0)
        print(self.row1)
        print(self.row2)
        print(self.row3)
        print(self.row4)
        print(self.row5)
        print(self.row6)
        print(self.row7)
        print(self.row8)
        print("")
        print("You put your map back in your backpack")

    def write_to_file(self):
        file = open("map_data.txt", "w")
        text_string = f"{self.row0} \n{self.row1} \n{self.row2} \n{self.row3} \n{self.row4} " \
                      f"\n{self.row5} \n{self.row6} \n{self.row7} \n{self.row8}"
        file.write(text_string)
        file.close()
