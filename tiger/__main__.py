import sys

from .commander import Commander
from .queue import TaskQueue

todo = TaskQueue()
commander = Commander(todo=todo)
commander.handle_command(sys.argv)
