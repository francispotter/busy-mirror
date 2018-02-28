'''
Move items to the top
'''

from .command import Command
from .item import Item
from .queue import Queue

class PopCommand(Command):

    command = 'pop'

    def do(itemtypename, arguments):
        itemclass, is_plural = Item.get_type(itemtypename)
        queue = Queue(itemclass)
        queue.load()
        indices = queue.indices(arguments, is_plural)
        queue.pop(indices)
        queue.save()

def run(): PopCommand.run(__name__)
run()
