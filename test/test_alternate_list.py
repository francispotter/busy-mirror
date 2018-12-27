from unittest import TestCase
from tempfile import TemporaryDirectory
from pathlib import Path
from unittest import mock
from io import StringIO
from datetime import date as Date
import unittest

from busy.plugins.todo import Task
from busy.commander import Commander

class TestAlternateList(TestCase):

    def test_get_from(self):
        with TemporaryDirectory() as t:
            p = Path(t, 'a.txt')
            p.write_text('b\n')
            c = Commander(root=t)
            o = c.handle('get','--queue','a')
            self.assertEqual(o, 'b')

    def test_default_queue(self):
        with TemporaryDirectory() as t:
            p = Path(t, 'todo.txt')
            p.write_text('b\n')
            c = Commander(root=t)
            o = c.handle('get')
            self.assertEqual(o, 'b')

    def test_add(self):
        with TemporaryDirectory() as t:
            c = Commander(root=t)
            with mock.patch('sys.stdin', StringIO('g')):
                c.handle('add','--queue','j')
                x = Path(t, 'j.txt').read_text()
                self.assertEqual(x, 'g\n')

    def test_drop(self):
        with TemporaryDirectory() as t:
            p = Path(t, 'u.txt')
            p.write_text('a\nb\nc\nd')
            c = Commander(root=t)
            c.handle('drop','2','4','--queue','u')
            o = p.read_text()
            self.assertEqual(o, 'a\nc\nb\nd\n')
