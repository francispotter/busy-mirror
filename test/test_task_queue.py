from unittest import TestCase

from tiger.queue import Queue
from tiger.task import Task

class TestQueue(TestCase):

    def test_task_list(self):
        q = Queue()
        q.add(Task('a'))
        q.add(Task('b'))
        i = q.list()
        self.assertEqual(str(i[0][1]), 'a')
