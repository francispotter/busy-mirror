from .queue import Queue

class TaskSet:

    def __init__(self, todo=None, plan=None):
        self.todo = todo or Queue()
        self.plan = plan or Queue()

    def _queue(self, task_type):
        if task_type=='todo':
            return self.todo
        elif task_type=='plan':
            return self.plan
        raise RuntimeError('Unknown task type %s' % task_type)

    def get(self, task_type='todo'):
        return self._queue(task_type).get()

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
