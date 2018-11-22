from csv import DictReader
from csv import DictWriter

from .queue import Queue

class File:

    def __init__(self, path, schema):
        self._path = path
        self._schema = schema
        if path.is_file():
            with open(path) as datafile:
                reader = DictReader(datafile, schema, delimiter="|")
                self.queue = Queue(*reader)

    @property
    def queue(self):
        if not hasattr(self, '_queue'): self._queue = Queue()
        return self._queue

    @queue.setter
    def queue(self, value):
        assert isinstance(value, Queue)
        self._queue = value

    def save(self):
        with open(self._path, 'w') as datafile:
            writer = DictWriter(datafile, self._schema, delimiter="|")
            for item in self.queue.all():
                values = dict([(f, getattr(item,f)) for f in self._schema])
                writer.writerow(values)

class TodoFile(File):

    def __init__(self, path):
        super().__init__(path, ['description'])

class PlanFile(File):

    def __init__(self, path):
        super().__init__(path, ['description', 'plan_date'])
