'''
Base task for commands
'''


import os
import sys
from argparse import ArgumentParser

from tiger.item import Item

class Command:

    # Define 'command' and 'default_type'

    type_choices = Item.get_type_names()

    # Define a "do" method in subclasses

    @classmethod
    def run(self):
        parser = ArgumentParser(prog=self.command)
        parser.add_argument('type', default=self.default_type,
            choices=self.type_choices, nargs='?')
        arguments, others = parser.parse_known_args()
        result = self.do(arguments.type, others)
        if result: print(result)
