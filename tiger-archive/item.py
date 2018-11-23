
import os
from datetime import datetime as DateTime

from busy.selector import Selector

class Item:

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
        self.date = DateTime.strptime(date, '%Y-%m-%d').date()
        self.task = task

    @property
    def text(self):
        return "%s | %s" % (self.date.strftime('%Y-%m-%d'), self.task)
