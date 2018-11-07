from unittest import TestCase
import datetime

from tiger.task import Task

class TestTask(TestCase):

    def test_task(self):
        t = Task('b')
        self.assertIsInstance(t, Task)

    def test_description_as_string(self):
        t = Task('a')
        self.assertEqual(t.description, 'a')

    def test_task_requires_description(self):
        with self.assertRaises(RuntimeError):
            t = Task('')

    def test_plan(self):
        t = Task('a')
        d = datetime.date(2018,12,1)
        t.convert_to_plan(d)

    def test_plan_as_tuple(self):
        t = Task('b')
        t.convert_to_plan((2018,12,1))
        self.assertEqual(t.plan_date.month, 12)

    def test_plan_requires_date(self):
        t = Task('c')
        with self.assertRaises(RuntimeError):
            t.convert_to_plan('foo')