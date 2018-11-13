from .queue import Queue
from .task import Task

class System:

    def __init__(self, *items):
        self._todos = Queue()
        self._plans = Queue()
        self.add_todos(*items)

    def get_todo(self, index=1):
        return self._todos.get(index)

    def select(self, *criteria):
        return self._todos.select(*criteria)

    def list_todos(self):
        return self._todos.list()

    def count_todos(self):
        return self._todos.count()

    def add_todos(self, *items):
        for item in items:
            task = item if isinstance(item, Task) else Task(item)
            self._todos.add(task)

    def defer(self, date):
        t = self._todos.get()
        t.convert_to_plan(date)
        self._plans.add(t)
        self._todos.remove(t)

    def pop(self):
        self._todos.pop()
