from unittest import TestCase
from tempfile import TemporaryDirectory

from todo.system import System
from todo.system_directory import SystemDirectory
from todo.queue_file import QueueFile

class TestSystemDirectory(TestCase):

    def test_system_directory(self):
        with TemporaryDirectory() as d:
            sd = SystemDirectory(d)
            s = sd.system
            self.assertIsInstance(s, System)

    def test_add_todo(self):
        with TemporaryDirectory() as td:
            sd1 = SystemDirectory(td)
            sd1.system.add_todos('a')
            sd1.save()
            sd2 = SystemDirectory(td)
            self.assertEqual(str(sd2.system.get_todo()),'a')
