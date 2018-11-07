'''
Move items to the bottom
'''

from ..command import Command
from ..item import Item
from ..queue import Queue

class DropCommand(Command):

    command = 'drop'

    def do(queue, arguments, plural=True):
        queue.load()
        if not (arguments or plural): arguments = [1]
        indices = queue.indices(arguments, plural)
        queue.drop(indices)
        queue.save()

def run(): DropCommand.run()
if __name__ == '__main__': run()