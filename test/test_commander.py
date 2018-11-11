from unittest import TestCase

from tiger.task import Task
from tiger.commander import Commander
from tiger.task_set import TaskSet

class TestCommander(TestCase):

    def test_list(self):
        q = TaskSet()
        q.add(Task('a'))
        c = Commander(q)
        o = c.handle_command('list')
        self.assertEqual('     1  a', o)

    def test_add(self):
        q = TaskSet()
        c = Commander(q)
        c.handle_command('add','--task','g')
        s = q.list()
        self.assertEqual(str(s[0][1]), 'g')

    def test_list_plans(self):
        s = TaskSet()
        t = Task('a')
        s.add(t)
        c = Commander(s)
        o = c.handle_command('list','--plan')
