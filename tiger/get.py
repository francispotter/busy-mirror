'''
View a single item or a list of items
'''

from .command import Command
from .item import Item

class GetCommand(Command):

    command = 'get'

    def do(itemtypename, arguments):
        selection = Item.get_selection(itemtypename, arguments)
        texts = [s.title for i,s in selection]
        return '\n'.join(texts)

GetCommand.run(__name__)
