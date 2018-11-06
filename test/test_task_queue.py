from unittest import TestCase

from tiger.queue import TaskQueue
from tiger.item import Task

class TestTaskQueue(TestCase):

    def test_task_list(self):
        q = TaskQueue()
        q.add(Task('a'))
        q.add(Task('b'))
        i = q.list()
        self.assertEqual(str(i[0][1]), 'a')
