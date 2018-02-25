
import os

from tiger.selector import Selector
from .queue import Queue

class Item:

    TYPES = {}

    @classmethod
    def register_type(self, newtype):
        self.TYPES[newtype.__name__.lower()] = (newtype, False)
        self.TYPES[newtype.filename.lower()] = (newtype, True)

    @classmethod
    def get_type(self, name):
        return self.TYPES[name.lower()]

    @classmethod
    def get_type_names(self):
        return self.TYPES.keys()

    # @classmethod
    # def load_collection(self):
    #     filename = os.path.join(directory(), self.filename + EXTENSION)
    #     if os.path.isfile(filename):
    #         with open(filename) as datafile:
    #             reader = DictReader(datafile, self.headings, delimiter="|")
    #             if reader:
    #                 return [self(**d) for d in reader]

    @classmethod
    def get_selection(self, itemtypename, arguments):
        itemclass, is_plural = self.get_type(itemtypename)
        queue = Queue(itemclass)
        queue.load()
        return queue.select(arguments, is_plural)

    @property
    def title(self):
        return self.text[0].capitalize() + self.text[1:]


class Task(Item):

    filename = 'tasks'
    headings = ['description']

    def __init__(self, description=''):
        self.description = description

    @property
    def text(self):
        return self.description

Item.register_type(Task)

class Plan(Item):

    filename = 'plans'
    headings = ['date', 'task']

    def __init__(self, date=None, task=None):
        self.date = date
        self.task = task

    @property
    def text(self):
        return "%s | %s" % (self.date, self.task)

Item.register_type(Plan)
