'''
View a single item or a list of items
'''


import os
import sys
import argparse
import re
from csv import DictReader

from tiger import get_collection

def do(type):
    items = get_collection('tasks',['task'])
    if items:
        return items[0]['task']

def run():
    parser = argparse.ArgumentParser(prog="get")
    parser.add_argument('type', default='task', choices=['task'], nargs='?')
    arguments, others = parser.parse_known_args()
    print(do(arguments.type))

if __name__=='__main__':
    run()
