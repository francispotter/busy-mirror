from unittest import TestCase

from tiger.task import Task

class TestTask(TestCase):

    def test_task(self):
        t = Task()
        self.assertIsInstance(t, Task)
