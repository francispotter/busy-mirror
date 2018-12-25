from ..commander import Command
from ..commander import Commander

class ManageCommand(Command):

    command = 'manage'

    def execute(self, parsed):
        self._system.manage(*parsed.criteria)

Commander.register(ManageCommand)
