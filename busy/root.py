from pathlib import Path
from tempfile import TemporaryDirectory

from .system import System
from .task import Task
from .file import TodoFile
from .file import PlanFile

class Root:

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value):
        assert not hasattr(self, '_path')
        path = Path(value) if isinstance(value, str) else value
        assert isinstance(path, Path) and path.is_dir()
        self._path = path

    def __init__(self, path = None):
        if path: self.path = path

    @property
    def system(self):
        if not hasattr(self, '_system'):
            self._todo_file = TodoFile(self.path)
            self._plan_file = PlanFile(self.path)
            todo_queue = self._todo_file.queue
            plan_queue = self._plan_file.queue
            self._system = System(todos=todo_queue, plans=plan_queue)
        return self._system

    def save(self):
        self._todo_file.save()
        self._plan_file.save()
