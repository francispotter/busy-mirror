from .queue import TodoQueue
from .queue import PlanQueue
from .task import Task

class System:

    def __init__(self, *items, todos=None, plans=None):
        self.todos = todos if todos else TodoQueue()
        self.plans = plans if plans else PlanQueue()
        self.add(*items)

    def add(self, *items):
        self.todos.add(*items)

    def pop(self, *criteria):
        self.todos.pop(*criteria)

    def drop(self, *criteria):
        self.todos.drop(*criteria)

    def delete(self, *criteria):
        self.todos.delete(*criteria)

    def defer(self, date, *criteria):
        indices = self.todos.select(*(criteria or [1]))
        plans = [self.todos.get(i+1).as_plan(date) for i in indices]
        self.plans.add(*plans)
        self.todos.delete(*criteria)

    def activate(self, *criteria, today=False):
        indices = self.plans.select(*criteria)
        tasks = [self.plans.get(i+1).as_todo() for i in indices]
        self.todos.add(*tasks)
        self.plans.delete(*criteria)
