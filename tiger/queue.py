'''
A set of items in order
'''

import os
from csv import DictReader

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
        return self.itemclass.filename


    def load(self):
        filename = os.path.join(directory(), self.filename + EXTENSION)
        if os.path.isfile(filename):
            with open(filename) as datafile:
                reader = DictReader(datafile, self.headings, delimiter="|")
                if reader:
                    self.items = [self.itemclass(**d) for d in reader]

    def select(self, arguments, is_plural=True):
        # mytype, is_plural = self.get_type(itemtypename)
        # items = mytype.load_collection()
        if self.items:
            default = None if is_plural else 1
            selector = Selector(arguments, default)
            indices = selector.indices([i.text for i in self.items])
            if indices:
                if not is_plural: indices = indices[:1]
                return [(i+1, self.items[i]) for i in indices]
