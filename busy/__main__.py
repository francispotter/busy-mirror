import sys

from .commander import Commander

from busy import PYTHON_VERSION

if sys.version_info < PYTHON_VERSION:
    msg = "Busy requires Python version %i.%i.%i or higher" % PYTHON_VERSION
    raise RuntimeError(msg)

print(Commander().handle(*sys.argv[1:]))
