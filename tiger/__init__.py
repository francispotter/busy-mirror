
import os
from csv import DictReader

DEFAULT_DIR = '~/.config/tiger'
DIR_ENV = 'TIGER_DIR'
EXTENSION = '.list'

def get_collection(name, columns):
    if DIR_ENV in os.environ:
        dirname = os.environ[DIR_ENV]
    else:
        dirname = DEFAULT_DIR
    dirdir = os.path.expanduser(dirname)
    if not os.path.exists(dirdir):
        os.makedirs(dirdir)
    if not os.path.isdir(dirdir):
        raise RuntimeError("No directory at %s" % dirdir)
    filename = os.path.join(dirdir, name + EXTENSION)
    if os.path.isfile(filename):
        with open(filename) as datafile:
            reader = DictReader(datafile, columns)
            items = [i for i in reader]
            return items
