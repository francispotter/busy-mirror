'''
A set of items in order
'''

import os
from csv import DictReader
from csv import DictWriter

from tiger import directory

from .selector import Selector
from .item import Item
from .item import Task
from .item import Plan


class Queue:

    ITEMCLASS = Item

    def __init__(self, filename):
        self.filename = filename
        self.items = []

    @property
    def headings(self):
        return self.ITEMCLASS.headings

    def load(self):
        if os.path.isfile(self.filename):
            with open(self.filename) as datafile:
                reader = DictReader(datafile, self.headings, delimiter="|")
                if reader:
                    self.items = [self.ITEMCLASS(**d) for d in reader if d]

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

    def item(self, index):
        return self.items[index]

    def selection(self, arguments, plural=True):
        return [self.item(i) for i in self.indices(arguments, plural)]

    def pop(self, indices):
        oldlist = self.items
        hilist = [t for i,t in enumerate(oldlist) if i in indices]
        lolist = [t for i,t in enumerate(oldlist) if i not in indices]
        self.items = hilist + lolist

class TypedQueue(Queue):

    TYPES = {}

    @classmethod
    def add_type(self, queueclass):
        for typename in queueclass.TYPENAMES:
            self.TYPES[typename] = (queueclass, queueclass.TYPENAMES[typename])

    @classmethod
    def parse_typename(self, typename):
        return self.TYPES[typename] if typename in self.TYPES else None


class TaskQueue(Queue):

    ITEMCLASS = Task
    TYPENAMES = {'tasks': True, 'task': False}

    def __init__(self):
        super().__init__(os.path.join(directory(), 'tasks.list'))

TypedQueue.add_type(TaskQueue)

class PlanQueue(Queue):

    ITEMCLASS = Plan
    TYPENAMES = {'plans': True, 'plan': False}

    def __init__(self):
        super().__init__(os.path.join(directory(), 'plans.list'))

TypedQueue.add_type(PlanQueue)
