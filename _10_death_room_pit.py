import super_death_room


class DeathRoomPit(super_death_room.DeathRoom):

    def room_script(self):
        print("player.")
        print(self.player.name)

        self.died = True




