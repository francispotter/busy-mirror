'''
Move items to the top
'''


import os
import sys

from tiger import parse_command
from tiger.item import Item

def do(itemtypename, arguments):
    selection = Item.get_selection(itemtypename, arguments)
    texts = [s.title for i,s in selection]
    return '\n'.join(texts)

def run():
    arguments, others = parse_command('pop', Item.get_type_names(), 'tasks')
    result = do(arguments.type, others)
    if result: print(result)

if __name__=='__main__':
    run()
