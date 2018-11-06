'''
Add some items
Argument specifies where in the queue to insert
Insertion will happen before the first item indicated
If nothing indicated, then the end of the queue
'''

import sys

from ..command import Command
from ..item import Item
from ..queue import Queue

class AddCommand(Command):

    command = 'add'

    def do(queue, arguments, plural=True):
        if arguments: raise RuntimeError("The 'add' command takes no arguments")
        queue.load()
        strings = [n.strip() for n in sys.stdin] if plural else [input()]
        queue.read(strings)
        queue.save()

def run(): AddCommand.run()
if __name__ == '__main__': run()
