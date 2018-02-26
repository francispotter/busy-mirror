'''
A set of items in order
'''

import os
from csv import DictReader
from csv import DictWriter

from tiger import directory

from .selector import Selector

EXTENSION = '.list'


class Queue:

    def __init__(self, itemclass):
        self.itemclass = itemclass
        self.items = []


    # Might want to move these to Queue as real properties

    @property
    def headings(self):
        return self.itemclass.headings

    @property
    def filename(self):
        return os.path.join(directory(), self.itemclass.filename + EXTENSION)

    def load(self):
        if os.path.isfile(self.filename):
            with open(self.filename) as datafile:
                reader = DictReader(datafile, self.headings, delimiter="|")
                if reader:
                    self.items = [self.itemclass(**d) for d in reader]

    def save(self):
        with open(self.filename, 'w') as datafile:
            writer = DictWriter(datafile, self.headings, delimiter="|")
            for item in self.items:
                writer.writerow(vars(item))

    def indices(self, arguments, is_plural=True):
        indices = []
        if self.items:
            default = None if is_plural else 1
            selector = Selector(arguments, default)
            indices = selector.indices([i.text for i in self.items])
            if indices:
                if not is_plural: indices = indices[:1]
        return indices

    def select(self, arguments, is_plural=True):
        return [(i+1, self.items[i]) for i in self.indices(arguments, is_plural)]

    def pop(self, indices):
        oldlist = self.items
        hilist = [t for i,t in enumerate(oldlist) if i in indices]
        lolist = [t for i,t in enumerate(oldlist) if i not in indices]
        self.items = hilist + lolist
