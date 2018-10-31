
from .queue import TaskQueue

class Commander:

    def __init__(self, todo=TaskQueue()):
        self._todo = todo

    def handle_command(self, *args):
        command = args[0]
        method = getattr(self._todo, command.lower())
        result = method()
        return self.handle_output(command, result)

    def handle_output(self, command, output):
        if command == 'list':
            texts = ["%6i  %s" % (i, t) for i,t in output]
            return '\n'.join(texts)
