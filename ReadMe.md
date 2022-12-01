# Path to Faylight<br/>
`This is a single player, adventure text-based game`<br/>
<br/><br/>

## Introduction
Path to Faylight is a text-based game written in python. Your car has broken down in the middle of the woods, miles from civilization, and you need to find a way home.



## User Documentation
#### Overview and rules
The goal is to navigate through the rooms and solve puzzles to reach an ending.
You have a backpack that can be accessed using "i".
The rooms can be moved between using n e s w.
Conversations and options are navigated using the letters or numbers given.

#### Game play
The room will have a script, then, if applicable, it will ask the user dialogue or action options. After the script is complete or the user chooses to move on, the program will ask them which room they would like to move to.
<br/>
MAP:<br/>

    [[' START'], ['------'], ['------'], ['------']]
    [['??????'], ['??????'], ['??????'], ['------']]
    [['??????'], ['??????'], ['??????'], ['------']]
    [['??????'], ['??????'], ['??????'], ['------']] 
    [['------'], ['??????'], ['??????'], ['??????']]
    [['------'], ['------'], ['??????'], ['------']] 
    [['------'], ['??????'], ['??????'], ['??????']] 
    [['------'], ['??????'], ['??????'], ['??????']] 
    [['------'], ['------'], ['??????'], ['------']]

## Developer Documentation
### Files and resources
- _0_starting_room
- _1_bug_room
- _2_fox_room
- _3_deer_room
- _4_mushroom_room
- _5_bug_puzzle_room_m
- _6_bug_puzzle_room_y
- _7_death_room_waterfall
- _8_flower_room_m
- _9_flower_room_y
- _10_death_room_pit
- _11_witch_house_room
- _12_witch_clearing_room
- _13_fae_encounter_room
- _14_crossroads_puzzle_room
- _15_death_room_wrong_way
- _16_fairy_clearing_room
- _17_human_ending_room.py
- _18_royal_ending_room
- _19_rave_ending_room
- backpack
- main
- map
- map_data
- player
- room
- rooms_info
- super_bug_room
- super_death_room
- super_flower_room

## User Requirements Specification

- 0. Starting Room - connects to room 1S
- 1. Bug Clearing - connects to room 2E3S
- 2. Fox Clearing - connects to room 4S
- 3. Deer Clearing - connects to room 4E
- 4. Mushroom Clearing - connects to room 5E6S
- 5. Bug Puzzle M -  connects to room 7N8S
- 6. Bug Puzzle Y - connects to room 9S10W
- 7. Death Room Waterfall - connects to room  DEATH
- 8. Flower Room Marigold - connects to room  12S
- 9. Flower Room Yarrow - connects to room  12E
- 10. Death Room Pit Trap - connects to room  9E or death
- 11. Witch's House - connects to room  13S
- 12. Witch's Clearing - connects to room  11E13W
- 13. Fae Encounter Path - connects to room  14S
- 14. Crossroads Puzzle - connects to room  15E16S15W
- 15. Wrong Way Death - connects to room  14W or death
- 16. Fairy Clearing - connects to room  17E18S19W
- 17. Human Ending
- 18. Royal Ending
- 19. Rave Ending

