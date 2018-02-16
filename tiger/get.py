'''
View a single item or a list of items
'''


import os
import sys
import argparse
import re
from csv import DictReader

from tiger import get_collection
from tiger.selector import Selector

def do(type, arguments):
    items = get_collection('tasks',['task'])
    if items:
        selector = Selector(arguments, 1)
        indices = selector.indices([i['task'] for i in items])
        if indices:
            results = [items[i]['task'] for i in indices]
            texts = [r[0].capitalize() + r[1:] for r in results]
            return '\n'.join(texts)

def run():
    parser = argparse.ArgumentParser(prog="get")
    parser.add_argument('type', default='task', choices=['task'], nargs='?')
    arguments, others = parser.parse_known_args()
    print(do(arguments.type, others))

if __name__=='__main__':
    run()
