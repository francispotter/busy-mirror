from ..commander import Command
from ..commander import Commander

class ListCommand(Command):

    command = 'list'

    @classmethod
    def register(self, parser):
        parser.add_argument('--plans', action='store_true')

    def execute(self, parsed):
        key = 'plan' if parsed.plans else 'todo'
        queue = self._root.get_queue(key)
        itemlist = queue.list(*parsed.criteria)
        return self._list(queue, itemlist)

Commander.register(ListCommand)
