from _0_starting_room import StartingRoom as Room0
from _1_bug_room import BugRoom as Room1
from _2_fox_room import FoxRoom as Room2
from _3_deer_room import DeerRoom as Room3
from _4_mushroom_room import MushroomRoom as Room4
from _5_bug_puzzle_room_m import BugPuzzleRoomM as Room5
from _6_bug_puzzle_room_y import BugPuzzleRoomY as Room6
from _7_death_room_waterfall import DeathRoomWaterfall as Room7

import player

player_object = player.Player()
room0 = Room0("start", 0, south=1)
room1 = Room1("bug", 1, east=2, south=3)
room2 = Room2("fox", 2, south=4)
room3 = Room3("deer", 3, east=4)
room4 = Room4("mushroom", 4, east=5, south=6)
room5 = Room5("bug puzzle m", 5, north=7, south=8)
room6 = Room6("bug puzzle y", 6, south=9, west=10)
room7 = Room7("death room waterfall", 7)

room_list = [room0, room1, room2, room3, room4, room5, room6, room7]
current_room = room_list[7]

game_running = True
restart_game = False


def game_instructions():
    ask = True
    while ask:
        print("Would you like to hear the game instructions?")
        print("Please enter Y for yes and N for no:")
        instruct = input("> ")
        if instruct.lower() == "y":
            print("GAME INSTRUCTIONS")
            ask = False
        elif instruct.lower() == "n":
            ask = False
        else:
            continue


def game_over():
    print("You died :(")
    ask = True
    while ask:
        print("Would you like to start the game again?")
        print("Please enter Y for yes and N for no:")
        instruct = input("> ")
        if instruct.lower() == "y":
            global current_room
            current_room = room_list[0]
            global restart_game
            restart_game = True
            return True
        elif instruct.lower() == "n":
            global game_running
            game_running = False
            print("Thank you for playing :)")
            return False
        else:
            continue


def test():
    print("________________________________________________________________")
    print(" Please enter one of the listed options to enter the next area ")
    print("________________________________________________________________")

if __name__ == "__main__":
    #test()
    print(f"Welcome to the game {player_object.name}")
    game_instructions()

    while game_running:
        restart_game = False
        current_room.room_script()
        item = current_room.room_actions()
        if item is not None:
            if item == "death":
                result = game_over()
                if not result:
                    continue
            else:
                player_object.add_to_backpack(item)
        if not restart_game:
            current_room = room_list[int(current_room.choose_next_room())]

    print("outside game")


