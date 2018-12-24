from argparse import ArgumentParser
from tempfile import TemporaryDirectory
import sys
from tempfile import TemporaryFile
from pathlib import Path
import importlib
import re

from .root import Root
from . import PYTHON_VERSION
import busy
from .todo import Task

class Commander:

    def __init__(self, *args, root=None):
        if sys.version_info < PYTHON_VERSION:
            message = ("Busy requires Python version %i.%i.%i or higher" %
                PYTHON_VERSION)
            raise RuntimeError(message)
        if root: self.root = Root(root)

    def handle(self, *args):
        parsed, remaining = self._parser.parse_known_args(args)
        parsed.criteria = remaining
        if parsed.root: self.root = Root(parsed.root)
        if hasattr(parsed, 'command'):
            command = parsed.command(self.root)
            result = command.execute(parsed)
            self.root.save()
            return result

    @property
    def root(self):
        if not hasattr(self, '_root'): self._root = Root()
        return self._root

    @root.setter
    def root(self, value):
        assert not hasattr(self, '_path')
        assert isinstance(value, Root)
        self._root = value

    @classmethod
    def register(self, command_class):
        if not hasattr(self, '_parser'):
            self._parser = ArgumentParser()
            self._parser.add_argument('--root', action='store')
            self._subparsers = self._parser.add_subparsers()
        subparser = self._subparsers.add_parser(command_class.command)
        subparser.set_defaults(command=command_class)
        command_class.register(subparser)


class Command:

    def __init__(self, root):
        self._root = root

    @property
    def _system(self):
        return self._root.system

    @classmethod
    def register(self, parser):
        pass

    def execute(self, parsed):
        method = getattr(self._system, self.command)
        result = method(*parsed.criteria)
        return result

    def _list(self, queue, tasklist):
        fmtstring = "{0:>6}  " + queue.listfmt
        texts = [fmtstring.format(i, t) for i,t in tasklist]
        return '\n'.join(texts)


commands_dir = Path(__file__).parent / 'commands'
for command_file in commands_dir.iterdir():
    if re.match(r'^[^_].*\_command\.py$', command_file.name):
        importlib.import_module(f'busy.commands.{command_file.stem}')
