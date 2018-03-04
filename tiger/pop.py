'''
Move items to the top
'''

from .command import Command
from .item import Item
from .queue import Queue

class PopCommand(Command):

    command = 'pop'

    def do(queue, arguments, plural=True):
        queue.load()
        indices = queue.indices(arguments, plural)
        queue.pop(indices)
        queue.save()

def run(): PopCommand.run(__name__)
run()
