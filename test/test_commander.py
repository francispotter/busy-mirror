from unittest import TestCase
from tempfile import TemporaryDirectory
from pathlib import Path

from busy.task import Task
from busy.commander import Commander
from busy.system import System

# class TestCommander(TestCase):

    # def test_list(self):
    #     c = Commander()
    #     c.system.add_todos(Task('a'))
    #     o = c.handle('list')
    #     self.assertEqual('     1  a', o)
#
#     def test_add(self):
#         c = Commander()
#         c.handle('add','--task','g')
#         s = c.system.list_todos()
#         self.assertEqual(str(s[0][1]), 'g')
#
#     def test_list_plans(self):
#         s = System()
#         t = Task('a')
#         s.add_todos(t)
#         c = Commander(s)
#         o = c.handle('list','--plan')
#
#     def test_root_option(self):
#         with TemporaryDirectory() as d:
#             c = Commander()
#             o = c.handle('--root',d,'add','--task','a')
#             p = Path(d) / 'todo.txt'
#             r = p.read_text()
#             assertEqual(r, 'a')
