

class Queue:

    def __init__(self):
        self._items = []

    def add(self, item):
        self._items.append(item)

    def list(self):
        return [(i+1, t) for i,t in enumerate(self._items)]

class TaskQueue(Queue):
    pass
