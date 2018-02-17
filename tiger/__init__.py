
import os
from argparse import ArgumentParser

DEFAULT_DIR = '~/.config/tiger'
DIR_ENV = 'TIGER_DIR'

def directory():
    if DIR_ENV in os.environ:
        dirname = os.environ[DIR_ENV]
    else:
        dirname = DEFAULT_DIR
    result = os.path.expanduser(dirname)
    if not os.path.exists(result):
        os.makedirs(result)
    if not os.path.isdir(result):
        raise RuntimeError("No directory at %s" % result)
    return result


def parse_command(command):
    parser = ArgumentParser(prog=command)
    parser.add_argument('type', default='task', choices=['task','tasks','plan'], nargs='?')
    return parser.parse_known_args()
