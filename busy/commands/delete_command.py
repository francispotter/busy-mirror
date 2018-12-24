from ..commander import Command
from ..commander import Commander

class DeleteCommand(Command):

    command = 'delete'

    @classmethod
    def register(self, parser):
        parser.add_argument('--yes', action='store_true')

    def execute(self, parsed):
        tasklist = self._system.todos.list(*parsed.criteria or [1])
        indices = [i[0]-1 for i in tasklist]
        if hasattr(parsed, 'yes') and parsed.yes:
            confirmed = True
        else:
            print('\n'.join([str(i[1]) for i in tasklist]))
            confirmed = input('Delete? (Y/n) ').startswith('Y')
        if not confirmed:
            print("Deletion must be confirmed")
        else:
            self._system.todos.delete_by_indices(*indices)
            self._root.save()

Commander.register(DeleteCommand)
