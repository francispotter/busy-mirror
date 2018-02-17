
import os
from csv import DictReader

from tiger import directory

EXTENSION = '.list'

class Item:

    TYPES = {}

    @classmethod
    def register_type(self, newtype):
        self.TYPES[newtype.__name__.lower()] = newtype

    @classmethod
    def get_type(self, name):
        return self.TYPES[name.lower()]

    @classmethod
    def load_collection(self):
        filename = os.path.join(directory(), self.filename + EXTENSION)
        if os.path.isfile(filename):
            with open(filename) as datafile:
                reader = DictReader(datafile, self.headings)
                if reader:
                    return [self(**d) for d in reader]

class Task(Item):

    is_plural = False
    filename = 'tasks'
    headings = ['description']

    def __init__(self, description=''):
        self.description = description

    @property
    def text(self):
        return self.description

Item.register_type(Task)

class Tasks(Task):

    is_plural = True

Item.register_type(Tasks)

class Plan(Item):

    is_plural = False
    filename = 'plans'
    headings = ['date', 'task']

    def __init__(self, date=None, task=None):
        self.date = date
        self.task = task

    @property
    def text(self):
        return self.date + ' | ' + self.task

Item.register_type(Plan)
