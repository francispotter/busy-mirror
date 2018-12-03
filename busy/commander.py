
from argparse import ArgumentParser
from tempfile import TemporaryDirectory

from .root import Root

class Commander:

    def __init__(self, *args, root=None):
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


class DropCommand(Command):

    command = 'drop'

    def execute(self, parsed):
        self._system.drop(*parsed.criteria)
        self._root.save()

Commander.register(DropCommand)


class PopCommand(Command):

    command = 'pop'

    def execute(self, parsed):
        self._system.pop(*parsed.criteria)
        self._root.save()

Commander.register(PopCommand)


class GetCommand(Command):

    command = 'get'

    def execute(self, parsed):
        if parsed.criteria:
            print("The `get` command only returns the active task - repeat without criteria")
        else:
            return str(self._system.todos.get() or '')

Commander.register(GetCommand)
