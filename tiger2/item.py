class Item:
    pass

class Task(Item):

    def __init__(self, description):
        self._description = description

    def __str__(self):
        return self._description
