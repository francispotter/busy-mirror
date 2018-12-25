from ..commander import Command
from ..commander import Commander

class GetCommand(Command):

    command = 'get'

    @classmethod
    def register(self, parser):
        parser.add_argument('--from', nargs=1, dest="list")

    def execute(self, parsed):
        if parsed.criteria:
            message = ("The `get` command only returns the top item - "
                "repeat without criteria")
            raise RuntimeError(message)
        else:
            key = parsed.list[0] if getattr(parsed, 'list') else 'todo'
            return str(self._root.get_queue(key).get() or '')

Commander.register(GetCommand)
