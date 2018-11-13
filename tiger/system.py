from .queue import Queue

class System:

    def __init__(self, *tasks):
        self.todo = Queue(*tasks)
        self.plan = Queue()

    def _queue(self, task_type):
        if task_type=='todo':
            return self.todo
        elif task_type=='plan':
            return self.plan
        raise RuntimeError('Unknown task type %s' % task_type)

    def get(self, task_type='todo', criteria=1):
        return self._queue(task_type).get(criteria)

    def select(self, *criteria):
        return self._queue('todo').select(*criteria)

    def list(self):
        return self.todo.list()

    def add(self, task):
        return self.todo.add(task)

    def defer(self, date):
        t = self.todo.get()
        t.convert_to_plan(date)
        self.plan.add(t)
        self.todo.remove(t)

    def pop(self):
        self.todo.pop()
