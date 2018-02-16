'''
View a single item or a list of items
'''


import os
import sys
import argparse
import re

def do(arg, **kwargs):
    return "Hello"

def run():
    parser = argparse.ArgumentParser(prog="view")
    options, arguments = parser.parse_known_args()
    for arg in arguments or ['']:
        print(do(arg, **vars(options)))

if __name__=='__main__':
    run()
