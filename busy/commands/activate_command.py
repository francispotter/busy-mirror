from ..commander import Command
from ..commander import Commander

class ActivateCommand(Command):

    command = 'activate'

    @classmethod
    def register(self, parser):
        parser.add_argument('--today','-t', action='store_true')

    def execute(self, parsed):
        if hasattr(parsed, 'today') and parsed.today:
            self._system.activate(today=True)
        else:
            self._system.activate(*parsed.criteria)
        self._root.save()

Commander.register(ActivateCommand)
