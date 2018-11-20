from unittest import TestCase
from tempfile import TemporaryDirectory

from todo.system import System
from todo.root import Root
from todo.file import File

class TestRoot(TestCase):

    def test_root(self):
        with TemporaryDirectory() as d:
            sd = Root(d)
            s = sd.system
            self.assertIsInstance(s, System)

    def test_add_todo(self):
        with TemporaryDirectory() as td:
            sd1 = Root(td)
            sd1.system.add_todos('a')
            sd1.save()
            sd2 = Root(td)
            self.assertEqual(str(sd2.system.get_todo()),'a')
