from .queue import TaskQueue
from .queue import PlanQueue

from .item import Plan

class Data:

    def __init__(self, todo=None, plan=None):
        self.todo = todo or TaskQueue()
        self.plan = plan or PlanQueue()

    def defer(self, date):
        t = self.todo.get()
        self.plan.add(Plan(date, t))
        self.todo.remove(t)
