'''
View a single item or a list of items with line numbers
'''

import os
import sys

from tiger import parse_command
from tiger.item import Item

def do(itemtypename, arguments):
    selection = Item.get_selection(itemtypename, arguments)
    texts = ["%6i  %s" % (i, s.title) for i,s in selection]
    return '\n'.join(texts)

def run():
    arguments, others = parse_command('list', Item.get_type_names(), 'tasks')
    result = do(arguments.type, others)
    if result: print(result)

if __name__=='__main__':
    run()
