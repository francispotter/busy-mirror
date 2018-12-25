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
            if getattr(parsed, 'list'):
                return "Hello world"
            return str(self._root.get_file('todo').queue.get() or '')

Commander.register(GetCommand)
