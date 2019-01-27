from csv import DictReader
from csv import DictWriter
from pathlib import Path

from .queue import Queue
from .item import Item

class File:

    def __init__(self, path):
        self._path = path

    @classmethod
    def read_items(self, fileish, itemclass=Item):
        reader = DictReader(fileish, itemclass.schema, delimiter="|")
        return [itemclass.create(i) for i in reader if i]

    def read(self, itemclass=Item):
        if self._path.is_file():
            with open(self._path) as datafile:
                return self.read_items(datafile, itemclass)
        return []

    @classmethod
    def write_items(self, fileish, *items):
        schema = items[0].schema
        writer = DictWriter(fileish, schema, delimiter="|")
        for item in items:
            values = dict([(f, getattr(item, f)) for f in schema])
            writer.writerow(values)


    def save(self, *items):
        if items:
            with open(self._path, 'w') as datafile:
                self.write_items(datafile, *items)
        else:
            Path(self._path).write_text('')
