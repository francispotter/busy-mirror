'''
View a single item or a list of items with line numbers
'''

from .command import Command
from .item import Item

class ListCommand(Command):

    command = 'list'

    def do(itemtypename, arguments):
        selection = Item.get_selection(itemtypename, arguments)
        texts = ["%6i  %s" % (i, s.title) for i,s in selection]
        return '\n'.join(texts)

def run(): ListCommand.run(__name__)
run()
