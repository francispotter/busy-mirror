from unittest import TestCase

from tiger.task import Task
from tiger.commander import Commander
from tiger.system import System

class TestCommander(TestCase):

    def test_list(self):
        q = System()
        q.add_todos(Task('a'))
        c = Commander(q)
        o = c.handle('list')
        self.assertEqual('     1  a', o)

    def test_add(self):
        q = System()
        c = Commander(q)
        c.handle('add','--task','g')
        s = q.list_todos()
        self.assertEqual(str(s[0][1]), 'g')

    def test_list_plans(self):
        s = System()
        t = Task('a')
        s.add_todos(t)
        c = Commander(s)
        o = c.handle('list','--plan')
