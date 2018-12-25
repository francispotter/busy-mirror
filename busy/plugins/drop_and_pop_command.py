from ..commander import Command
from ..commander import Commander

class DropCommand(Command): command = 'drop'
Commander.register(DropCommand)

class PopCommand(Command): command = 'pop'
Commander.register(PopCommand)
