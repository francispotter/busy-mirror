from ..commander import Command
from ..commander import Commander

class ManageCommand(Command):

    command = 'manage'

    def execute(self, parsed):
        key = 'todo'
        self._root.get_queue(key).manage(*parsed.criteria)

Commander.register(ManageCommand)
