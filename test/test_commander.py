from unittest import TestCase

from tiger2.queue import TaskQueue
from tiger2.item import Task
from tiger2.commander import Commander

class TestCommander(TestCase):

    def test_list(self):
        q = TaskQueue()
        q.add(Task('a'))
        c = Commander(todo=q)
        o = c.handle_command('list')
        self.assertEqual('     1  a', o)
