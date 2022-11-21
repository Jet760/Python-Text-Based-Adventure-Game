import super_flower_room


class FlowerRoomM(super_flower_room.FlowerRoom):
    def __init__(self, name, number, north=None, east=None, south=None, west=None):
        super().__init__(name, number, "marigold", north, east, south, west)
