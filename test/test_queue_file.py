from unittest import TestCase
from pathlib import Path

from tiger.queue_file import QueueFile
from tiger.queue import Queue
from tiger.task import Task
from tiger.task import TODO_SCHEMA

class TestQueueFile(TestCase):

    def test_load_tasks(self):
        p = Path(__file__).parent.joinpath('test_tasks.txt')
        f = QueueFile(p, Task, TODO_SCHEMA)
        q = f.load()
        self.assertIsInstance(q, Queue)
        self.assertEqual(str(q.get()), 'a')

    def test_load_if_not_there(self):
        p = Path(__file__).parent.joinpath('not_there.txt')
        f = QueueFile(p, Task, TODO_SCHEMA)
        q = f.load()
        self.assertIsInstance(q, Queue)
        self.assertEqual(q.count(), 0)
