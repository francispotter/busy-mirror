from csv import DictReader
from csv import DictWriter
from pathlib import Path

from .queue import Queue
from .item import Item

class File:

    def __init__(self, path):
        self._path = path

    def read(self, itemclass=Item):
        if self._path.is_file():
            with open(self._path) as datafile:
                reader = DictReader(datafile, itemclass.schema, delimiter="|")
                return [itemclass.create(i) for i in reader if i]
        return []

    def save(self, *items):
        if items:
            schema = items[0].schema
            with open(self._path, 'w') as datafile:
                writer = DictWriter(datafile, schema, delimiter="|")
                for item in items:
                    values = dict([(f, getattr(item, f)) for f in schema])
                    writer.writerow(values)
        else:
            Path(self._path).write_text('')
