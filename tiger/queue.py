'''
A set of items in order
Indices are all zero-based
'''

import os
from csv import DictReader
from csv import DictWriter

from .selector import Selector
from .item import Item
from .item import Task
from .item import Plan

DEFAULT_DIR = '~/.config/tiger'
DIR_ENV = 'TIGER_DIR'


class Queue:

    TYPES = {}

    @classmethod
    def add_type(self, queueclass):
        for typename in queueclass.typenames:
            self.TYPES[typename] = (queueclass, queueclass.typenames[typename])

    @classmethod
    def parse_typename(self, typename):
        return self.TYPES[typename] if typename in self.TYPES else None

    @classmethod
    def get_typenames(self):
        return self.TYPES.keys()

    @classmethod
    def default_directory(self):
        if DIR_ENV in os.environ:
            dirname = os.environ[DIR_ENV]
        else:
            dirname = DEFAULT_DIR
        result = os.path.expanduser(dirname)
        if not os.path.exists(result):
            os.makedirs(result)
        if not os.path.isdir(result):
            raise RuntimeError("No directory at %s" % result)
        return result

    def __init__(self, filename=None):
        if not filename:
            if not self.default_filename:
                raise RuntimeError("No queue specified")
            directory = self.default_directory()
            filename = os.path.join(directory, self.default_filename)
        self.filename = filename
        self.items = []

    @property
    def headings(self):
        return self.itemclass.headings

    def load(self):
        if os.path.isfile(self.filename):
            with open(self.filename) as datafile:
                self.read(datafile)

    def read(self, stream):
        reader = DictReader(stream, self.headings, delimiter="|")
        if reader:
            self.items += [self.itemclass(**d) for d in reader if d]

    def save(self):
        with open(self.filename, 'w') as datafile:
            writer = DictWriter(datafile, self.headings, delimiter="|")
            for item in self.items:
                writer.writerow(vars(item))

    def indices(self, arguments, plural=False):
        indices = []
        if self.items:
            selector = Selector(arguments)
            indices = selector.indices([i.text for i in self.items])
            indices = indices[:1] if (indices and not plural) else indices
        return indices

    def item(self, index):
        return self.items[index]

    def selection(self, arguments, plural=True):
        return [self.item(i) for i in self.indices(arguments, plural)]

    def split(self, indices):
        inlist = [t for i,t in enumerate(self.items) if i in indices]
        outlist = [t for i,t in enumerate(self.items) if i not in indices]
        return (inlist, outlist)


    # The basic operations

    def pop(self, indices):
        hilist, lolist = self.split(indices)
        self.items = hilist + lolist

    def drop(self, indices):
        lolist, hilist = self.split(indices)
        self.items = hilist + lolist

    def delete(self, indices):
        killlist, keeplist = self.split(indices)
        self.items = keeplist

    @property
    def length(self): return len(self.items)

class ItemQueue(Queue):

    itemclass = Item
    typenames = {'items': True, 'item': False}
    default_filename = None

Queue.add_type(ItemQueue)

class TaskQueue(Queue):

    itemclass = Task
    typenames = {'tasks': True, 'task': False}
    default_filename = 'tasks.list'

Queue.add_type(TaskQueue)

class PlanQueue(Queue):

    itemclass = Plan
    typenames = {'plans': True, 'plan': False}
    default_filename = 'plans.list'

Queue.add_type(PlanQueue)
