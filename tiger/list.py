'''
View a single item or a list of items with line numbers
'''

from .command import Command
from .item import Item

class ListCommand(Command):

    command = 'list'

    def do(queue, arguments, plural=True):
        queue.load()
        indices = queue.indices(arguments, plural)
        texts = ["%6i  %s" % (i+1, queue.item(i).title) for i in indices]
        return '\n'.join(texts)

def run(): ListCommand.run()
if __name__ == '__main__': run()
