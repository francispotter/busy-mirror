from unittest import TestCase
from tempfile import TemporaryDirectory
from pathlib import Path

from busy.system import System
from busy.root import Root
from busy.file import File

class TestRoot(TestCase):

    def test_root(self):
        with TemporaryDirectory() as d:
            sd = Root(Path(d))
            s = sd.system
            self.assertIsInstance(s, System)

    def test_add_todo(self):
        with TemporaryDirectory() as td:
            sd1 = Root(Path(td))
            sd1.system.add('a')
            sd1.save()
            sd2 = Root(Path(td))
            self.assertEqual(str(sd2.system.todos.get()),'a')

    def test_make_dir_pater(self):
        r = Root()
        with TemporaryDirectory() as td:
            r.path = Path(td)
            r.system.add('a')
            r.save()
            r2 = Root(Path(td))
            self.assertEqual(str(r2.system.todos.get()),'a')
