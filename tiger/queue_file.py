from csv import DictReader

from .queue import Queue
from .task import Task

class QueueFile:

    def __init__(self, path):
        self._path = path

    def load(self):
        headings = ['description']
        if self._path.is_file():
            with open(self._path) as datafile:
                reader = DictReader(datafile, headings, delimiter="|")
                if reader:
                    tasks = [Task(**d) for d in reader if d]
                    return Queue(*tasks)
        return Queue()
