'''
View a single item or a list of items
'''


import os
import sys
from argparse import ArgumentParser

from .command import Command
from tiger.item import Item

class GetCommand(Command):

    command = 'get'

    def do(itemtypename, arguments):
        selection = Item.get_selection(itemtypename, arguments)
        texts = [s.title for i,s in selection]
        return '\n'.join(texts)


if __name__=='__main__':
    GetCommand.run()
