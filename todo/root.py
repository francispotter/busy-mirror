from pathlib import Path

from .system import System
from .task import Task
from .task import TODO_SCHEMA
from .task import PLAN_SCHEMA
from .file import File

TODO_FILE_NAME = 'todo.txt'
PLAN_FILE_NAME = 'plan.txt'

class Root:

    def __init__(self, directory):
        assert Path(directory).is_dir()
        self._directory = Path(directory)
        self._todo_file = self._file(TODO_FILE_NAME, TODO_SCHEMA)
        self._plan_file = self._file(PLAN_FILE_NAME, PLAN_SCHEMA)
        todo_queue = self._todo_file.queue
        plan_queue = self._plan_file.queue
        self.system = System(todos=todo_queue, plans=plan_queue)

    def _file(self, filename, schema):
        path = self._directory / filename
        return File(path, Task, schema)

    def save(self):
        self._todo_file.save()
        self._plan_file.save()
