from unittest import TestCase
from tempfile import TemporaryDirectory
from pathlib import Path
from unittest import mock
from io import StringIO
from datetime import date as Date

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

    def test_drop(self):
        with TemporaryDirectory() as t:
            p = Path(t, 'todo.txt')
            p.write_text('a\nb\nc\nd')
            c = Commander(root=t)
            c.handle('drop','2','4')
            o = p.read_text()
            self.assertEqual(o, 'a\nc\nb\nd\n')

    def test_pop(self):
        with TemporaryDirectory() as t:
            p = Path(t, 'todo.txt')
            p.write_text('a\nb\nc\nd')
            c = Commander(root=t)
            c.handle('pop','2','4')
            o = p.read_text()
            self.assertEqual(o, 'b\nd\na\nc\n')

    def test_get(self):
        with TemporaryDirectory() as t:
            p = Path(t, 'todo.txt')
            p.write_text('a\nb\nc\nd')
            c = Commander(root=t)
            o = c.handle('get')
            self.assertEqual(o, 'a')

    def test_get_if_no_tasks(self):
        with TemporaryDirectory() as t:
            c = Commander(root=t)
            o = c.handle('get')
            self.assertEqual(o, '')

    def test_delete(self):
        with TemporaryDirectory() as t:
            p = Path(t, 'todo.txt')
            p.write_text('a\nb\nc\nd')
            c = Commander(root=t)
            c.handle('delete','--yes','3-')
            o = p.read_text()
            self.assertEqual(o, 'a\nb\n')

    def test_delete_with_input_confirmation_yes(self):
        with TemporaryDirectory() as t:
            p = Path(t, 'todo.txt')
            p.write_text('a\nb\nc\nd')
            c = Commander(root=t)
            with mock.patch('sys.stdin', StringIO('Y')):
                c.handle('delete','3-')
                o = p.read_text()
                self.assertEqual(o, 'a\nb\n')

    def test_delete_with_input_confirmation_no(self):
        with TemporaryDirectory() as t:
            p = Path(t, 'todo.txt')
            p.write_text('a\nb\nc\nd')
            c = Commander(root=t)
            with mock.patch('sys.stdin', StringIO('no')):
                c.handle('delete','3-')
                o = p.read_text()
                self.assertEqual(o, 'a\nb\nc\nd')

    def test_defer(self):
        with TemporaryDirectory() as t:
            p = Path(t, 'todo.txt')
            p.write_text('a\nb\nc\nd')
            c = Commander(root=t)
            c.handle('defer','2','--to','2019-09-06')
            o = p.read_text()
            self.assertEqual(o, 'a\nc\nd\n')
            o2 = Path(t, 'plan.txt').read_text()
            self.assertEqual(o2, '2019-09-06|b\n')

    def test_defer_for(self):
        with TemporaryDirectory() as t:
            p = Path(t, 'todo.txt')
            p.write_text('a\nb\nc\nd')
            c = Commander(root=t)
            c.handle('defer','2','--for','2019-09-06')
            o = p.read_text()
            self.assertEqual(o, 'a\nc\nd\n')
            o2 = Path(t, 'plan.txt').read_text()
            self.assertEqual(o2, '2019-09-06|b\n')

    def test_defer_days(self):
        with TemporaryDirectory() as t:
            p = Path(t, 'todo.txt')
            p.write_text('a\nb\nc\nd')
            with mock.patch('busy.future.today', lambda : Date(2019,2,11)):
                c = Commander(root=t)
                c.handle('defer','2','--for','1 day')
                o = p.read_text()
                self.assertEqual(o, 'a\nc\nd\n')
                o2 = Path(t, 'plan.txt').read_text()
                self.assertEqual(o2, '2019-02-12|b\n')

    def test_defer_d(self):
        with TemporaryDirectory() as t:
            p = Path(t, 'todo.txt')
            p.write_text('a\nb\nc\nd')
            with mock.patch('busy.future.today', lambda : Date(2019,2,11)):
                c = Commander(root=t)
                c.handle('defer','2','--for','5d')
                o = p.read_text()
                self.assertEqual(o, 'a\nc\nd\n')
                o2 = Path(t, 'plan.txt').read_text()
                self.assertEqual(o2, '2019-02-16|b\n')

    def test_get_with_criteria(self):
        with TemporaryDirectory() as t:
            p = Path(t, 'todo.txt')
            p.write_text('a\nb\nc\nd')
            c = Commander(root=t)
            with self.assertRaises(RuntimeError):
                c.handle('get','3-4')
