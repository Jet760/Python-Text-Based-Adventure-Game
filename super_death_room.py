import room


class DeathRoom(room.Room):
    def __init__(self, name, number, north=None, east=None, south=None, west=None):
        super().__init__(name, number, north, east, south, west)
        self.died = False

    def room_actions(self):
        if self.died:
            return "death"

        else:
            return None





