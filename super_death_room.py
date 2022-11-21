import room


class DeathRoom(room.Room):
    def __init__(self, name, number, player, north=None, east=None, south=None, west=None):
        super().__init__(name, number, north, east, south, west)
        self.died = False
        self.player = player

    def room_actions(self):
        if self.died:
            return "death"

        else:
            return None





