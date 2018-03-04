
import os

from tiger.selector import Selector

class Item:

    TYPES = {}
    headings = ['text']


    def __init__(self, text=''):
        self.text = text

    @property
    def title(self):
        return self.text[0].capitalize() + self.text[1:]


class Task(Item):

    headings = ['description']

    def __init__(self, description=''):
        self.description = description

    @property
    def text(self):
        return self.description

class Plan(Item):

    headings = ['date', 'task']

    def __init__(self, date=None, task=None):
        self.date = date
        self.task = task

    @property
    def text(self):
        return "%s | %s" % (self.date, self.task)
