'''
Move items to the bottom
'''

from .command import Command
from .item import Item
from .queue import Queue

class ClearCommand(Command):

    command = 'clear'

    def do(queue, arguments, plural=True):
        queue.load()
        if not (arguments or plural): arguments = [1]
        indices = queue.indices(arguments, plural)
        queue.drop(indices)
        queue.save()

def run(): DropCommand.run(__name__)
run()
