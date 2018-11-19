from csv import DictReader
from csv import DictWriter

from .queue import Queue

class QueueFile:

    def __init__(self, path, item_class, schema):
        self._path = path
        self._item_class = item_class
        self._schema = schema

    def load(self):
        if self._path.is_file():
            with open(self._path) as datafile:
                reader = DictReader(datafile, self._schema, delimiter="|")
                if reader:
                    tasks = [self._item_class(**d) for d in reader if d]
                    return Queue(*tasks)
        return Queue()

    def save(self, queue):
        with open(self._path, 'w') as datafile:
            writer = DictWriter(datafile, self._schema, delimiter="|")
            for item in queue.all():
                values = dict([(f, getattr(item,f)) for f in self._schema])
                writer.writerow(values)
