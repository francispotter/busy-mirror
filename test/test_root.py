from unittest import TestCase
from tempfile import TemporaryDirectory
from pathlib import Path

from todo.system import System
from todo.root import Root
from todo.file import File

class TestRoot(TestCase):

    def test_root(self):
        with TemporaryDirectory() as d:
            sd = Root(Path(d))
            s = sd.system
            self.assertIsInstance(s, System)

    def test_add_todo(self):
        with TemporaryDirectory() as td:
            sd1 = Root(Path(td))
            sd1.system.add_todos('a')
            sd1.save()
            sd2 = Root(Path(td))
            self.assertEqual(str(sd2.system.get_todo()),'a')

    def test_make_dir_pater(self):
        r = Root()
        with TemporaryDirectory() as td:
            r.path = Path(td)
            r.system.add_todos('a')
            r.save()
            r2 = Root(Path(td))
            self.assertEqual(str(r2.system.get_todo()),'a')
