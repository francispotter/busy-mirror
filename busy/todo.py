# Functionality specific to todo queues and plans

from .queue import Queue
from .item import Item

import busy.future
import busy
from .file import File

TODO_STATE = 't'
PLAN_STATE = 'p'
DONE_STATE = 'd'

class Task(Item):

    def __init__(self, description=None, plan_date=None):
        super().__init__(description)
        self._state = TODO_STATE
        if plan_date: self.as_plan(plan_date)

    def as_plan(self, date):
        self._state = PLAN_STATE
        self._plan_date = busy.future.absolute_date(date)
        return self

    def as_todo(self):
        self._state = TODO_STATE
        return self

    @property
    def plan_date(self):
        return self._plan_date

    @property
    def project(self):
        tags = self.tags
        return tags[0] if tags else None


class TodoQueue(Queue):
    itemclass = Task

    def defer(self, date, *criteria):
        indices = self.select(*(criteria or [1]))
        plans = [self.get(i+1).as_plan(date) for i in indices]
        self.plans.add(*plans)
        self.delete_by_indices(*indices)


class PlanQueue(TodoQueue):
    schema = ['plan_date', 'description']
    listfmt = "{1.plan_date:%Y-%m-%d}  {1.description}"

    def activate(self, *criteria, today=False):
        if today:
            func = lambda t: t.plan_date <= busy.future.today()
            indices = self.select(func)
        else:
            indices = self.select(*criteria)
        tasks = [self.get(i+1).as_todo() for i in indices]
        self.todos.add(*tasks, index=0)
        self.delete_by_indices(*indices)


class System:

    def __init__(self, *items, todos=None, plans=None):
        self.plans = plans if plans else PlanQueue()
        self.todos = todos if todos else TodoQueue()
        self.todos.plans = self.plans
        self.plans.todos = self.todos
        self.add(*items)

    def add(self, *items):
        self.todos.add(*items)

    def pop(self, *criteria):
        self.todos.pop(*criteria)

    def drop(self, *criteria):
        self.todos.drop(*criteria)

    def defer(self, date, *criteria):
        self.todos.defer(date, *criteria)

    def activate(self, *criteria, today=False):
        self.plans.activate(*criteria, today=today)

    def manage(self, *criteria):
        self.todos.manage(*criteria)

class TodoFile(File):
    queueclass = TodoQueue
    slug = 'todo'

class PlanFile(File):
    queueclass = PlanQueue
    slug = 'plan'
