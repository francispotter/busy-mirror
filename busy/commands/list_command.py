from ..commander import Command
from ..commander import Commander

class ListCommand(Command):

    command = 'list'

    @classmethod
    def register(self, parser):
        parser.add_argument('--plans', action='store_true')

    def execute(self, parsed):
        queue = self._system.plans if parsed.plans else self._system.todos
        tasklist = queue.list(*parsed.criteria)
        return self._list(queue, tasklist)

Commander.register(ListCommand)
