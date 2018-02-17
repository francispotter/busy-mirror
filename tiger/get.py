'''
View a single item or a list of items
'''


import os
import sys
import argparse
import re
from csv import DictReader

from tiger import parse_command
from tiger.selector import Selector
from tiger.item import Item

def do(itemtype, arguments):
    mytype = Item.get_type(itemtype)
    is_plural = mytype.is_plural
    items = mytype.load_collection()
    if items:
        default = None if is_plural else 1
        selector = Selector(arguments, default)
        indices = selector.indices([i.text for i in items])
        if indices:
            if not is_plural: indices = indices[:1]
            results = [items[i].text for i in indices]
            texts = [r[0].capitalize() + r[1:] for r in results]
            return '\n'.join(texts)

def run():
    arguments, others = parse_command('get')
    result = do(arguments.type, others)
    if result: print(result)

if __name__=='__main__':
    run()
