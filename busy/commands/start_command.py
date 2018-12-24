from ..commander import Command
from ..commander import Commander

class StartCommand(Command):

    command = 'start'

    @classmethod
    def register(self, parser):
        parser.add_argument('project', action='store', nargs='?')

    def execute(self, parsed):
        if parsed.criteria:
            raise RuntimeError('Start takes only an optional project name')
        self._system.activate(today=True)
        queue = self._system.todos
        if queue.count() < 1:
            raise RuntimeError('There are no active tasks')
        project = parsed.project or queue.get().project
        if not project:
            raise RuntimeError('The `start` command required a project')
        self._system.manage(project)
        result = queue.pop(project)


Commander.register(StartCommand)
