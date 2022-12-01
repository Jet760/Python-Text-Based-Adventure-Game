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
from _11_witch_house_room import WitchHouseRoom as Room11
from _12_witch_clearing_room import WitchClearingRoom as Room12
from _13_fae_encounter_room import FaeEncounterRoom as Room13
from _14_crossroads_puzzle_room import CrossRoadsRoom as Room14
from _15_death_room_wrong_way import DeathRoomWrongWay as Room15
from _16_fairy_clearing_room import FairyClearingRoom as Room16
from _17_human_ending_room import HumanEndingRoom as Room17
from _18_royal_ending_room import RoyalEndingRoom as Room18
from _19_rave_ending_room import RaveEndingRoom as Room19

import backpack
import player
#import map

map = map.Map()
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
room8 = Room8(player_object, "flower m", 8, south=12)
room9 = Room9(player_object, "flower y", 9, east=12)
room10 = Room10(player_object, "death room pit", 10, east=9)
room11 = Room11(player_object, "witch house", 11, west=12)
room12 = Room12(player_object, "witch garden", 12, west=13)
room13 = Room13(player_object, "fae encounter", 13, south=14)
room14 = Room14(player_object, "cross roads puzzle", 14, west=15, south=16, east=15)
room15 = Room15(player_object, "death room wrong way", 15, west=14)
room16 = Room16(player_object, "fairy clearing", 16)
room17 = Room17(player_object, "human ending", 17)
room18 = Room18(player_object, "royal ending", 18)
room19 = Room19(player_object, "rave ending", 19)
room20 = Room4(player_object, "ending mushroom", 20, south=16)

room_list = [room0, room1, room2, room3, room4, room5, room6, room7, room8, room9, room10, room11, room12, room13,
             room14, room15, room16, room17, room18, room19, room20]
current_room = room_list[16]

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
            for room in room_list:
                room.has_been_visited = False
            return True
        elif instruct.lower() == "n":
            global game_running
            game_running = False
            print("Thank you for playing :)")
            return False
        else:
            continue

def ending():
    print("Thanks for playing!")
    print("Hope you had fun :)")
    self.map.clear()
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
            for room in room_list:
                room.has_been_visited = False
            return True
        elif instruct.lower() == "n":
            global game_running
            game_running = False
            print("Bye!")
            return False
        else:
            continue


def test():
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
    #backpack.add("marigold")
    backpack.add("yarrow")
    backpack.add("rope")
    #backpack.add("scarlet_elf_cup")
    #backpack.add("fly_agaric")
    #backpack.add("common_puffball")


if __name__ == "__main__":
    test()
    print(f"Welcome to the game {player_object.name}")
    game_instructions()

    while game_running:
        if restart_game:
            backpack.reset()
        restart_game = False
        current_room.room_script()
        item = current_room.room_actions()
        if item is not None:
            if item == "death":
                result = game_over()
                if not result:
                    continue
            if item == "ending":
                ending()
            else:
                player_object.add_to_backpack(item)
        if not restart_game:
            current_room = room_list[int(current_room.choose_next_room())]

    print("outside game")
