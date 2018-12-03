from .queue import TodoQueue
from .queue import PlanQueue
from .task import Task

class System:

    def __init__(self, *items, todos=None, plans=None):
        self.todos = todos if todos else TodoQueue()
        self.plans = plans if plans else PlanQueue()
        self.add(*items)

    def list(self, which='todo', criteria=[]):
        queue = getattr(self, f'{which}s')
        return queue.list(*criteria), queue

    def add(self, *items):
        self.todos.add(*items)

    def defer(self, date, *criteria):
        indices = self.todos.select(*(criteria or [1]))
        plans = [self.todos.get(i+1).as_plan(date) for i in indices]
        self.plans.add(*plans)
        self.todos.delete(*criteria)

    def pop(self):
        self.todos.pop()
