
from argparse import ArgumentParser

from .queue import TaskQueue
from .item import Task

class Command:

    @classmethod
    def register(self, subparser_set):
        subparser = subparser_set.add_parser(self.command)
        subparser.set_defaults(command=self)
        return subparser

    @classmethod
    def arguments(self, parsed):
        return {}

    @classmethod
    def output(self, result):
        return result

PARSER = ArgumentParser()
subparser_set = PARSER.add_subparsers()

class ListCommand(Command):

    command = 'list'

    @classmethod
    def output(self, result):
        texts = ["%6i  %s" % (i, t) for i,t in result]
        return '\n'.join(texts)


ListCommand.register(subparser_set)

class AddCommand(Command):

    command = 'add'

    @classmethod
    def register(self, subparser_set):
        subparser = super().register(subparser_set)
        subparser.add_argument('--task')

    @classmethod
    def arguments(self, parsed):
        result = super().arguments(parsed)
        if hasattr(parsed, 'task'):
            task = Task(parsed.task)
        else:
            task = Task(input('Task: '))
        result['task'] = task
        return result


AddCommand.register(subparser_set)


class Commander:

    def __init__(self, todo=TaskQueue()):
        self._todo = todo

    def handle_command(self, *args):
        parsed = PARSER.parse_args(args)
        command = parsed.command
        method = getattr(self._todo, command.command.lower())
        arguments = command.arguments(parsed)
        result = method(**arguments)
        return command.output(result)
