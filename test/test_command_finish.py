from unittest import TestCase
from tempfile import TemporaryDirectory
from pathlib import Path
from unittest import mock
from io import StringIO
from datetime import date as Date
import unittest

from busy.commander import Commander

class TestCommandFinish(TestCase):

    def test_finish(self):
        with TemporaryDirectory() as t:
            p = Path(t, 'tasks.txt')
            p.write_text('a\n')
            c = Commander(root=t)
            with mock.patch('busy.future.today', lambda : Date(2019,2,11)):
                c.handle('finish','--yes')
                o = Path(t, 'done.txt').read_text()
                self.assertEqual(o, '2019-02-11|a\n')

    def test_confirmation(self):
        with TemporaryDirectory() as t:
            p = Path(t, 'tasks.txt')
            p.write_text('a\n')
            c = Commander(root=t)
            o = StringIO()
            with mock.patch('busy.future.today', lambda : Date(2019,2,11)):
                with mock.patch('sys.stdin', StringIO('Y')):
                    with mock.patch('sys.stdout', o):
                        c.handle('finish')
                        o = Path(t, 'done.txt').read_text()
                        self.assertEqual(o, '2019-02-11|a\n')