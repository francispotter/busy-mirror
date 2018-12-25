from ..commander import Command
from ..commander import Commander

class ManageCommand(Command):

    command = 'manage'

    def execute(self, parsed):
        slug = 'todo'
        self._root.get_queue(slug).manage(*parsed.criteria)

Commander.register(ManageCommand)
