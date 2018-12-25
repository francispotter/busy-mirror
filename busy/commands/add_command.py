from ..commander import Command
from ..commander import Commander

class AddCommand(Command):

    command = 'add'

    @classmethod
    def register(self, parser):
        parser.add_argument('--task')

    def execute(self, parsed):
        if hasattr(parsed, 'task') and parsed.task:
            task = parsed.task
        else:
            task = input('Task: ')
        slug = 'todo'
        self._root.get_queue(slug).add(task)

Commander.register(AddCommand)
