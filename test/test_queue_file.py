from unittest import TestCase
from pathlib import Path

from tiger.queue_file import QueueFile
from tiger.queue import Queue

class TestQueueFile(TestCase):

    def test_load(self):
        p = Path(__file__).parent.joinpath('test_tasks.txt')
        f = QueueFile(p)
        q = f.load()
        self.assertIsInstance(q, Queue)
        self.assertEqual(str(q.get()), 'a')
