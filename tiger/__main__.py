import sys

from .commander import Commander
from .queue import Queue

todo = Queue()
commander = Commander(todo=todo)
commander.handle_command(sys.argv)
