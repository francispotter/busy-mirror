'''
Base task for commands
'''


import os
import sys
from argparse import ArgumentParser

from .item import Item
from .queue import Queue
from .queue import TypedQueue

class Command:

    # Define 'command'

    type_choices = Item.get_type_names()

    # Define a "do" method in subclasses


    # Method that's called when run from the command line.

    @classmethod
    def run(self, module=None):
        if module == '__main__':
            parser = ArgumentParser(prog=self.command)
            parser.add_argument('--queue', '-q', action='store')
            parser.add_argument('type', choices=self.type_choices, nargs='?')
            arguments, others = parser.parse_known_args()
            if arguments.queue:
                queue = Queue(arguments.queue)
                plural = True
            elif arguments.type:
                queuetype, plural = TypedQueue.parse_typename(arguments.type)
                queue = queuetype()
            else:
                raise RuntimeError('No queue or type specified')
            result = self.do(queue, others, plural)
            if result: print(result)
