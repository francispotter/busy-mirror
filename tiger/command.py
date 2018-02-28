'''
Base task for commands
'''


import os
import sys
from argparse import ArgumentParser

from tiger.item import Item

class Command:

    # Define 'command'

    type_choices = Item.get_type_names()

    # Define a "do" method in subclasses


    # Method that's called when run from the command line.

    @classmethod
    def run(self, module=None):
        if module == '__main__':
            parser = ArgumentParser(prog=self.command)
            parser.add_argument('type', choices=self.type_choices)
            arguments, others = parser.parse_known_args()
            result = self.do(arguments.type, others)
            if result: print(result)
