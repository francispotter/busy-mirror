from .queue import Queue
from .queue import Queue

from .task import Plan

class TaskSet:

    def __init__(self, todo=None, plan=None):
        self.todo = todo or Queue()
        self.plan = plan or Queue()

    def add_todo(self, task):
        self.todo.add(task)

    def get_todo(self):
        return self.todo.get()

    def list(self):
        return self.todo.list()

    def add(self, task):
        return self.todo.add(task)

    def defer(self, date):
        t = self.todo.get()
        self.plan.add(Plan(date, t))
        self.todo.remove(t)
