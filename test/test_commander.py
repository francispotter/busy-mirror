from unittest import TestCase
from tempfile import TemporaryDirectory
from pathlib import Path
from unittest import mock
from io import StringIO

from busy.task import Task
from busy.commander import Commander
from busy.system import System

class TestCommander(TestCase):

    def test_with_root_param(self):
        with TemporaryDirectory() as t:
            c = Commander(root=t)
            o = c.handle('add','--task','a')
            x = Path(t, 'todo.txt').read_text()
            self.assertEqual(x, 'a\n')

    def test_with_root_option(self):
        with TemporaryDirectory() as t:
            c = Commander()
            c.handle('--root', t)
            c.handle('add','--task','a')
            x = Path(t, 'todo.txt').read_text()
            self.assertEqual(x, 'a\n')

    def test_list(self):
        with TemporaryDirectory() as t:
            c = Commander(root=t)
            c.handle('add','--task','a')
            o = c.handle('list')
            self.assertEqual(o, '     1  a')

    def test_add_by_input(self):
        with TemporaryDirectory() as t:
            c = Commander(root=t)
            with mock.patch('sys.stdin', StringIO('g')):
                c.handle('add')
                x = Path(t, 'todo.txt').read_text()
                self.assertEqual(x, 'g\n')

    def test_list_plans(self):
        with TemporaryDirectory() as t:
            p = Path(t, 'plan.txt')
            p.write_text('2019-01-04|g\n2019-02-05|p')
            c = Commander(root=t)
            o = c.handle('list','--plan')
            self.assertEqual(o, '     1  2019-01-04  g\n     2  2019-02-05  p')

    def test_list_with_criteria(self):
        with TemporaryDirectory() as t:
            p = Path(t, 'todo.txt')
            p.write_text('a\nb\nc\nd')
            c = Commander(root=t)
            o = c.handle('list','2','4')
            self.assertEqual(o, '     2  b\n     4  d')


#
#     def test_add(self):
#         c = Commander()
#         c.handle('add','--task','g')
#         s = c.system.list_todos()
#         self.assertEqual(str(s[0][1]), 'g')
#
#     def test_root_option(self):
#         with TemporaryDirectory() as d:
#             c = Commander()
#             o = c.handle('--root',d,'add','--task','a')
#             p = Path(d) / 'todo.txt'
#             r = p.read_text()
#             assertEqual(r, 'a')
