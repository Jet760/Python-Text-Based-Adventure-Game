import super_flower_room


class FlowerRoomY(super_flower_room.FlowerRoom):
    def __init__(self, name, number, north=None, east=None, south=None, west=None):
        super().__init__(name, number, "yarrow", north, east, south, west)
