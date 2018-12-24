from csv import DictReader
from csv import DictWriter

from .queue import TodoQueue
from .queue import PlanQueue
from .queue import Queue

class File:

    queueclass = Queue

    def __init__(self, dirpath, slug=None):
        self._path = dirpath / f'{slug or self.slug}.txt'
        if self._path.is_file():
            with open(self._path) as datafile:
                reader = DictReader(datafile, self.schema, delimiter="|")
                self.queue = self.queueclass(*reader)

    @property
    def queue(self):
        if not hasattr(self, '_queue'): self._queue = self.queueclass()
        return self._queue

    @queue.setter
    def queue(self, value):
        assert isinstance(value, self.queueclass)
        self._queue = value

    @property
    def schema(self):
        return self.queueclass.schema

    def save(self):
        with open(self._path, 'w') as datafile:
            writer = DictWriter(datafile, self.schema, delimiter="|")
            for item in self.queue.all():
                values = dict([(f, getattr(item,f)) for f in self.schema])
                writer.writerow(values)

class TodoFile(File):
    queueclass = TodoQueue
    slug = 'todo'

class PlanFile(File):
    queueclass = PlanQueue
    slug = 'plan'
