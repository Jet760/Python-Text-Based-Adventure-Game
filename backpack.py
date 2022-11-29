class BackPack:
    """
    BackPack Class

    """

    def __init__(self, items=None):
        self._backpack = []
        if items is None:
            items = []
        #if type(items) is not "<class 'list'>":
            #items = []
        for item in items:
            self._backpack.append(item)
        self.sort()

    def sort(self):
        self._backpack.sort()

    def count(self):
        return len(self._backpack)

    def list(self):
        print("You open your backpack and have a look inside")
        if self.count() >= 1:
            self.sort()
            print("The backpack contains:")
            print(self._backpack)
        else:
            print("The backpack is empty")
        print("You zip back up your backpack")

    def add(self, item):
        if item is not None:
            self._backpack.append(item)
            self.sort()

    def in_backpack(self, item):
        """
        Complete this method using a binary search
        returns -1 or False if not found
        returns position if found
        :param item:
        :return: -1 | False | integer
        """
        low = 0
        high = self.count() - 1
        self.sort()
        return self.binary_search(item, low, high)

    def binary_search(self, item, low, high):
        if low > high:
            return False
        else:
            mid = int((low + high) / 2)
            if item == self._backpack[mid]:
                return mid
            elif item > self._backpack[mid]:
                return self.binary_search(item, mid + 1, high)
            else:
                return self.binary_search(item, low, mid - 1)

    def remove_item(self, item):
        if item is not None:
            position = self.in_backpack(item)
            if position != False:
                self._backpack.pop(position)

    def get_item_name(self, position):
        if position is not None or position is not False:
            return self._backpack[position]
        else:
            return False

    def reset(self):
        self._backpack = []
