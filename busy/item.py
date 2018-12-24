from datetime import date as Date
from datetime import datetime as DateTime
from datetime import timedelta as TimeDelta
import re

class Item:

    def __init__(self, description=None):
        assert isinstance(description, str)
        assert description
        self._description = description

    def __str__(self):
        return self._description

    @property
    def description(self):
        return self._description

    @classmethod
    def create(self, value):
        if isinstance(value, self):
            return value
        elif isinstance(value, str):
            return self(value)
        elif isinstance(value, dict):
            return self(**value)

    @property
    def tags(self):
        words = self.description.split()
        return [w[1:].lower() for w in words if w.startswith('#')]
