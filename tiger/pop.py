'''
Move items to the top
'''


import os
import sys

from tiger import parse_command
from .item import Item
from .queue import Queue

def do(itemtypename, arguments):
    itemclass, is_plural = Item.get_type(itemtypename)
    queue = Queue(itemclass)
    queue.load()
    indices = queue.indices(arguments, is_plural)
    queue.pop(indices)
    queue.save()

def run():
    arguments, others = parse_command('pop', Item.get_type_names(), 'tasks')
    result = do(arguments.type, others)
    if result: print(result)

if __name__=='__main__':
    run()
