
from .item import Task

class Queue:

    def __init__(self):
        self._items = []

    def add(self, item='', **kwargs):
        self._items.append(item)

    def list(self, **kwargs):
        return [(i+1, t) for i,t in enumerate(self._items)]

class TaskQueue(Queue):

    def add(self, task='', **kwargs):
        assert isinstance(task, Task)
        self._items.append(task)
