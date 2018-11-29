import sys

from .commander import Commander
from . import PYTHON_VERSION

def main():
    if sys.version_info < PYTHON_VERSION:
        msg = "Busy requires Python version %i.%i.%i or higher" % PYTHON_VERSION
        raise RuntimeError(msg)
    print(Commander().handle(*sys.argv[1:]))

main()
