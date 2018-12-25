# A queue manager, which happens to use the file system

from pathlib import Path
from tempfile import TemporaryDirectory
import os

from .file import File
from .queue import Queue

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

    def get_queue(self, slug):
        if slug not in self._open_files:
            queueclass = Queue.subclass(slug)
            queuefile = File(self.path, slug=slug, queueclass=queueclass)
            self._open_files[slug] = queuefile
        return self._open_files[slug].queue

    def save(self):
        while self._open_files:
            self._open_files.popitem()[1].save()


    # DEPRECATED

    @property
    def system(self):
        if not hasattr(self, '_system'):
            from .plugins.todo import System
            todos = self.get_queue('todo')
            plans = self.get_queue('plan')
            self._system = System(todos=todos, plans=plans)
        return self._system
