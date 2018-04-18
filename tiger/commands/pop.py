'''
Move items to the top
'''

from ..command import Command
from ..item import Item
from ..queue import Queue

class PopCommand(Command):

    command = 'pop'

    def do(queue, arguments, plural=True):
        queue.load()
        if not (arguments or plural): arguments = [queue.length]
        indices = queue.indices(arguments, plural)
        queue.pop(indices)
        queue.save()

def run(): PopCommand.run()
if __name__ == '__main__': run()
