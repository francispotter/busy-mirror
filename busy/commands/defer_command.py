from ..commander import Command
from ..commander import Commander
from ..future import date_for

class DeferCommand(Command):

    command = 'defer'

    @classmethod
    def register(self, parser):
        parser.add_argument('--to','--for',dest='time_info')

    def execute(self, parsed):
        tasklist = self._system.todos.list(*parsed.criteria or [1])
        indices = [i[0]-1 for i in tasklist]
        if hasattr(parsed, 'time_info') and parsed.time_info:
            time_info = parsed.time_info
        else:
            print('\n'.join([str(i[1]) for i in tasklist]))
            time_info = input('Defer to [tomorrow]: ').strip() or 'tomorrow'
        self._root.system.defer(date_for(time_info), *parsed.criteria)
        self._root.save()

Commander.register(DeferCommand)
