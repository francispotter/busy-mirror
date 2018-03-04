'''
View a single item or a list of items
'''

from .command import Command
from .item import Item

class GetCommand(Command):

    command = 'get'

    def do(queue, arguments, plural=True):
        queue.load()
        selection = queue.selection(arguments, plural)
        texts = [s.text for s in selection]
        return '\n'.join(texts)

def run(): GetCommand.run()
if __name__ == '__main__': run()
