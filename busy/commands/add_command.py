from ..commander import QueueCommand
from ..commander import Commander

class AddCommand(QueueCommand):

    command = 'add'

    @classmethod
    def register(self, parser):
        super().register(parser)
        parser.add_argument('--task')

    def execute_on_queue(self, parsed, queue):
        if hasattr(parsed, 'task') and parsed.task:
            task = parsed.task
        else:
            task = input('Task: ')
        queue.add(task)

Commander.register(AddCommand)
