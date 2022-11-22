from _0_starting_room import StartingRoom as Room0
from _1_bug_room import BugRoom as Room1
from _2_fox_room import FoxRoom as Room2
from _3_deer_room import DeerRoom as Room3
from _4_mushroom_room import MushroomRoom as Room4
from _5_bug_puzzle_room_m import BugPuzzleRoomM as Room5
from _6_bug_puzzle_room_y import BugPuzzleRoomY as Room6
from _7_death_room_waterfall import DeathRoomWaterfall as Room7
from _8_flower_room_m import FlowerRoomM as Room8
from _9_flower_room_y import FlowerRoomY as Room9
from _10_death_room_pit import DeathRoomPit as Room10

import backpack
import player

backpack = backpack.BackPack()
player_object = player.Player(backpack)
room0 = Room0(player_object, "start", 0, south=1)
room1 = Room1(player_object, "bug", 1, east=2, south=3)
room2 = Room2(player_object, "fox", 2, south=4)
room3 = Room3(player_object, "deer", 3, east=4)
room4 = Room4(player_object, "mushroom", 4, east=5, south=6)
room5 = Room5(player_object, "bug puzzle m", 5, north=7, south=8)
room6 = Room6(player_object, "bug puzzle y", 6, south=9, west=10)
room7 = Room7(player_object, "death room waterfall", 7)
room8 = Room8(player_object, "flower m", 8, south=11)
room9 = Room9(player_object, "flower y", 9, east=11)
room10 = Room10(player_object, "death room pit", 10, east=9)

room_list = [room0, room1, room2, room3, room4, room5, room6, room7, room8, room9, room10]
current_room = room_list[10]

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
    backpack.add("a")
    backpack.add("c")
    backpack.add("b")
    backpack.add("h")
    backpack.add("j")
    backpack.add("jb")
    backpack.add("k")
    backpack.add("ba")
    backpack.add("bb")
    backpack.add("x")
    backpack.add("y")
    backpack.add("z")
    backpack.add("rope")


if __name__ == "__main__":
    test()
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
