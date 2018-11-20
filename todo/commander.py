
from argparse import ArgumentParser

from .queue import Queue
from .task import Task
from .system import System

class Commander:

    def __init__(self, system=System()):
        self._system = system

    def handle(self, *args):
        parsed = self._parser.parse_args(args)
        command = parsed.command(self._system)
        return command.execute(parsed)

    @classmethod
    def register(self, command_class):
        if not hasattr(self, '_parser'):
            self._parser = ArgumentParser()
            self._subparsers = self._parser.add_subparsers()
        subparser = self._subparsers.add_parser(command_class.command)
        subparser.set_defaults(command=command_class)
        command_class.register(subparser)


class Command:

    def __init__(self, system):
        self._system = system

class ListCommand(Command):

    command = 'list'

    @classmethod
    def register(self, parser):
        parser.add_argument('--plans', action='store_true')

    def execute(self, parsed):
        result = self._system.list_todos()
        texts = ["%6i  %s" % (i, t) for i,t in result]
        return '\n'.join(texts)

Commander.register(ListCommand)


class AddCommand(Command):

    command = 'add'

    @classmethod
    def register(self, parser):
        parser.add_argument('--task')

    def execute(self, parsed):
        if hasattr(parsed, 'task'):
            task = Task(parsed.task)
        else:
            task = Task(input('Task: '))
        self._system.add_todos(task)

Commander.register(AddCommand)
