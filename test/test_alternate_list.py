from unittest import TestCase
from tempfile import TemporaryDirectory
from pathlib import Path
from unittest import mock
from io import StringIO
from datetime import date as Date
import unittest

from busy.plugins.todo import Task
from busy.commander import Commander
from busy.plugins.todo import System

class TestAlternateList(TestCase):

    @unittest.skip("Alternate list")
    def test_get_from(self):
        with TemporaryDirectory() as t:
            p = Path(t, 'a.txt')
            p.write_text('b\n')
            c = Commander(root=t)
            o = c.handle('get','--from','movies')
            self.assertEqual(o, 'b')
