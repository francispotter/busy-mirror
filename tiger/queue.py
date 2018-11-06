
from .item import Task
from .item import Plan

class Queue:

    def __init__(self):
        self._items = []

    def add(self, item='', **kwargs):
        self._items.append(item)

    def get(self):
        return self._items[0] if self._items else None

    def list(self, **kwargs):
        return [(i+1, t) for i,t in enumerate(self._items)]

    def remove(self, items):
        if isinstance(items, list):
            for item in items:
                self._items.remove(item)
        else:
            self._items.remove(items)

class TaskQueue(Queue):

    def add(self, task='', **kwargs):
        assert isinstance(task, Task)
        self._items.append(task)

class PlanQueue(Queue):

    def add(self, plan):
        assert isinstance(plan, Plan)
        self._items.append(plan)
