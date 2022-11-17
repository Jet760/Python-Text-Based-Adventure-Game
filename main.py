from _0_starting_room import StartingRoom as Room0
from _1_bug_room import BugRoom as Room1
from _2_fox_room import FoxRoom as Room2
from _3_deer_room import DeerRoom as Room3
from _4_mushroom_room import MushroomRoom as Room4

import player

player_object = player.Player()
room0 = Room0("start", 0, south=1)
room1 = Room1("bug", 1, east=2, south=3)
room2 = Room2("fox", 2, south=4)
room3 = Room3("deer", 3, east=4)
room4 = Room4("mushroom", 4, east=5, south=6)

room_list = [room0, room1, room2, room3, room4]
current_room = room_list[0]

game_running = True

def game_instructions():
    ask = True
    while ask:
        print("Would you like to hear the game instructions?")
        print("Please enter Y for yes and N for no:")
        instruct = input("> ")
        if instruct.lower() == "y":
            print("GAME INSTRUSTIIONSSSS")
            ask = False
        elif instruct.lower() == "n":
            ask = False
        else:
            continue


def game_over():
    pass


def test():
    print("________________________________________________________________")
    print(" Please enter one of the listed options to enter the next area ")
    print("________________________________________________________________")

if __name__ == "__main__":
    #test()
    print(f"Welcome to the game {player_object.name}")
    game_instructions()

    while game_running:
        current_room.room_script()
        item = current_room.room_actions()
        if item is not None:
            if item == "death":
                game_over()
            else:
                player_object.add_to_backpack(item)
        current_room = room_list[int(current_room.choose_next_room())]



