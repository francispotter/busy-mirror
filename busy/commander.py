from argparse import ArgumentParser
from tempfile import TemporaryDirectory
import sys

from .root import Root
from . import PYTHON_VERSION

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
            return command.execute(parsed)

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
        self._root.save()
        return result

class ListCommand(Command):

    command = 'list'

    @classmethod
    def register(self, parser):
        parser.add_argument('--plans', action='store_true')

    def execute(self, parsed):
        queue = self._system.plans if parsed.plans else self._system.todos
        tasklist = queue.list(*parsed.criteria)
        fmtstring = "{0:>6}  " + queue.listfmt
        texts = [fmtstring.format(i, t) for i,t in tasklist]
        return '\n'.join(texts)

Commander.register(ListCommand)


class AddCommand(Command):

    command = 'add'

    @classmethod
    def register(self, parser):
        parser.add_argument('--task')

    def execute(self, parsed):
        if hasattr(parsed, 'task') and parsed.task:
            task = parsed.task
        else:
            task = input('Task: ')
        self._root.system.add(task)
        self._root.save()

Commander.register(AddCommand)


class DropCommand(Command): command = 'drop'
Commander.register(DropCommand)


class PopCommand(Command): command = 'pop'
Commander.register(PopCommand)


class DeleteCommand(Command):

    command = 'delete'

    @classmethod
    def register(self, parser):
        parser.add_argument('--yes', action='store_true')

    def execute(self, parsed):
        if hasattr(parsed, 'yes') and parsed.yes:
            confirmed = True
        else:
            confirmed = input('Delete? (Y/n) ').startswith('Y')
        if not confirmed:
            print("Deletion must be confirmed")
        else:
            self._root.system.delete(*parsed.criteria)
            self._root.save()

Commander.register(DeleteCommand)


class GetCommand(Command):

    command = 'get'

    def execute(self, parsed):
        if parsed.criteria:
            message = ("The `get` command only returns the active task - "
                "repeat without criteria")
            raise RuntimeError(message)
        else:
            return str(self._system.todos.get() or '')

Commander.register(GetCommand)


class DeferCommand(Command):

    command = 'defer'

    @classmethod
    def register(self, parser):
        parser.add_argument('--to','--for',dest='time_info')

    def execute(self, parsed):
        if hasattr(parsed, 'time_info') and parsed.time_info:
            date = parsed.time_info
        self._root.system.defer(date, *parsed.criteria)
        self._root.save()

Commander.register(DeferCommand)
