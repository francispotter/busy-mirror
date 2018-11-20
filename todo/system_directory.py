from pathlib import Path

from .system import System
from .task import Task
from .task import TODO_SCHEMA
from .task import PLAN_SCHEMA
from .queue_file import QueueFile

TODO_FILE_NAME = 'todo.txt'
PLAN_FILE_NAME = 'plan.txt'

class SystemDirectory:

    def __init__(self, directory):
        assert Path(directory).is_dir()
        self._directory = Path(directory)
        self._todo_file = self._queue_file(TODO_FILE_NAME, TODO_SCHEMA)
        self._plan_file = self._queue_file(PLAN_FILE_NAME, PLAN_SCHEMA)
        self._todo_queue = self._todo_file.load()
        self._plan_queue = self._plan_file.load()
        self.system = System(todos=self._todo_queue, plans=self._plan_queue)

    def _queue_file(self, filename, schema):
        path = self._directory / filename
        return QueueFile(path, Task, schema)

    def save(self):
        self._todo_file.save(self._todo_queue)
        self._plan_file.save(self._plan_queue)
