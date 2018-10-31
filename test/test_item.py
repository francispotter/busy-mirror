from unittest import TestCase

from tiger.item import Task

class TestItem(TestCase):

    def test_task_description(self):
        t = Task('d')
        self.assertEqual(t.description, 'd')
