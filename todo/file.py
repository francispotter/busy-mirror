from csv import DictReader
from csv import DictWriter

from .queue import Queue

class File:

    def __init__(self, path, item_class, schema):
        self._path = path
        self._item_class = item_class
        self._schema = schema
        if path.is_file():
            with open(path) as datafile:
                reader = DictReader(datafile, schema, delimiter="|")
                items = [item_class(**d) for d in reader if d] if reader else []
                self.queue = Queue(*items)
        else:
            self.queue = Queue()

    def save(self):
        with open(self._path, 'w') as datafile:
            writer = DictWriter(datafile, self._schema, delimiter="|")
            for item in self.queue.all():
                values = dict([(f, getattr(item,f)) for f in self._schema])
                writer.writerow(values)
