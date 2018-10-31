'''
Base task for commands
'''


import os
import sys
from argparse import ArgumentParser

from .item import Item
from .queue import Queue
from .queue import TaskQueue

class Command:

    # Define 'command'
    # Define a "do" method in subclasses

    # Method that's called when run from the command line.

    @classmethod
    def run(self):
        parser = ArgumentParser(prog=self.command)
        parser.add_argument('--queue', '-q', action='store')
        parser.add_argument('type', choices=Queue.get_typenames(),
            nargs='?', default='items')
        arguments, others = parser.parse_known_args()
        queuetype, plural = Queue.parse_typename(arguments.type)
        queue = queuetype(arguments.queue)
        result = self.do(queue, others, plural)
        if result: print(result)

def active():
    queue = TaskQueue()
    queue.load()
    task = queue.active_task()
    return task.text

def tiger():
    parser = ArgumentParser()
    parser.add_argument('command', choices=['active'],
        default='active', nargs='?')
    arguments, others = parser.parse_known_args()
    if arguments.command == 'active':
        print(active())
