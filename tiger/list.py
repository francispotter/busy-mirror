'''
View a single item or a list of items with line numbers
'''

import os
import sys

from .command import Command

from tiger.item import Item

class ListCommand(Command):

    command = 'list'

    def do(itemtypename, arguments):
        selection = Item.get_selection(itemtypename, arguments)
        texts = ["%6i  %s" % (i, s.title) for i,s in selection]
        return '\n'.join(texts)

if __name__=='__main__':
    ListCommand.run()
