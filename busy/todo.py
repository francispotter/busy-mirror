from .queue import Queue
from .item import Item

import busy.future
import busy


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


class PlanQueue(TodoQueue):
    schema = ['plan_date', 'description']
    listfmt = "{1.plan_date:%Y-%m-%d}  {1.description}"


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

    def defer(self, date, *criteria):
        indices = self.todos.select(*(criteria or [1]))
        plans = [self.todos.get(i+1).as_plan(date) for i in indices]
        self.plans.add(*plans)
        self.todos.delete_by_indices(*indices)

    def activate(self, *criteria, today=False):
        if today:
            func = lambda t: t.plan_date <= busy.future.today()
            indices = self.plans.select(func)
        else:
            indices = self.plans.select(*criteria)
        tasks = [self.plans.get(i+1).as_todo() for i in indices]
        self.todos.add(*tasks, index=0)
        self.plans.delete_by_indices(*indices)

    def manage(self, *criteria):
        tasklist = self.todos.list(*criteria)
        indices = [i[0]-1 for i in tasklist]
        before = ''.join([str(i[1])+'\n' for i in tasklist])
        after = busy.editor(before).split('\n')
        new_tasks = [Task(i) for i in after if i]
        self.todos.replace(indices, new_tasks)
