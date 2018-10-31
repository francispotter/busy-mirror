from unittest import TestCase

from tiger.queue import ItemQueue
from tiger.queue import TaskQueue
from tiger.item import Task

class TestQueue(TestCase):

    def test_read(self):
        q = ItemQueue('f')
        q.read(['a'])
        v = q.item(0).text
        self.assertEqual(v, 'a')

    def test_task_queue(self):
        q = TaskQueue()
        q.read(['a'])
        t = q.item(0)
        self.assertIsInstance(t, Task)

    def test_active_task(self):
        q = TaskQueue()
        q.read(['a','b'])
        a = q.active_task()
        self.assertEqual(a.description, 'a')

    def test_active_task_if_none(self):
        q = TaskQueue()
        a = q.active_task()
        self.assertIsNone(a)
