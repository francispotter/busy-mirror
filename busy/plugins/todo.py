from ..queue import Queue
from ..item import Item
from ..file import File
from ..commander import Command
from ..commander import Commander
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
    key = 'todo'

    def defer(self, date, *criteria):
        indices = self.select(*(criteria or [1]))
        plans = [self.get(i+1).as_plan(date) for i in indices]
        self.plans.add(*plans)
        self.delete_by_indices(*indices)

Queue.register(TodoQueue)

class TodoFile(File):
    slug = 'todo'

    def __init__(self, dirpath, slug=None):
        super().__init__(dirpath, slug='todo', queueclass=TodoQueue)

File.register(TodoFile)

class PlanQueue(Queue):
    itemclass = Task
    key = 'plan'
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

Queue.register(PlanQueue)

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

class PlanFile(File):
    slug = 'plan'

    def __init__(self, dirpath, slug=None):
        super().__init__(dirpath, slug='plan', queueclass=PlanQueue)


File.register(PlanFile)

class StartCommand(Command):

    command = 'start'

    @classmethod
    def register(self, parser):
        parser.add_argument('project', action='store', nargs='?')

    def execute(self, parsed):
        if parsed.criteria:
            raise RuntimeError('Start takes only an optional project name')
        self._system.activate(today=True)
        queue = self._system.todos
        if queue.count() < 1:
            raise RuntimeError('There are no active tasks')
        project = parsed.project or queue.get().project
        if not project:
            raise RuntimeError('The `start` command required a project')
        self._system.manage(project)
        result = queue.pop(project)


Commander.register(StartCommand)
