from .queue import Queue
from .task import Task

class System:

    def __init__(self, *items, todos=None, plans=None):
        self._todos = todos if todos else Queue()
        self._plans = plans if plans else Queue()
        self.add_todos(*items)

    def get_todo(self, index=1):
        return self._todos.get(index)

    def get_plan(self, index):
        return self._plans.get(index)

    def select(self, *criteria):
        return self._todos.select(*criteria)

    def list_todos(self): return self._todos.list()

    def list_plans(self): return self._plans.list()

    def count_todos(self): return self._todos.count()

    def count_plans(self): return self._plans.count()

    def add_todos(self, *items): self._todos.add(*items)

    def defer(self, date, *criteria):
        indices = self._todos.select(*(criteria or [1]))
        plans = [self._todos.get(i+1).as_plan(date) for i in indices]
        self._plans.add(*plans)
        self._todos.delete(*criteria)

    def pop(self):
        self._todos.pop()
