from pathlib import Path
from tempfile import TemporaryDirectory
import os

from .file import File

class Root:

    def __init__(self, path=None):
        if path: self.path = path
        self._open_files = {}

    @property
    def path(self):
        if not hasattr(self, '_path'):
            env_var = os.environ.get('BUSY_ROOT')
            self._path = Path(env_var if env_var else Path.home() / '.busy')
            if not self._path.is_dir(): self._path.mkdir()
        return self._path

    @path.setter
    def path(self, value):
        assert not hasattr(self, '_path')
        path = Path(value) if isinstance(value, str) else value
        assert isinstance(path, Path) and path.is_dir()
        self._path = path

    def get_file(self, slug):
        if slug not in self._open_files:
            self._open_files[slug] = File.open(self.path, slug)
        return self._open_files[slug]

    def get_queue(self, slug):
        return self.get_file(slug).queue

    @property
    def system(self):
        if not hasattr(self, '_system'):
            from .plugins.todo import System
            self._todo_file = self.get_file('todo')
            self._plan_file = self.get_file('plan')
            # self._todo_file = TodoFile(self.path)
            # self._plan_file = PlanFile(self.path)
            todos = self._todo_file.queue
            plans = self._plan_file.queue
            self._system = System(todos=todos, plans=plans)
        return self._system

    def save(self):
        while self._open_files:
            self._open_files.popitem()[1].save()
