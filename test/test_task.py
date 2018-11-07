from unittest import TestCase
import datetime

from tiger.task import Task

class TestTask(TestCase):

    def test_task(self):
        t = Task()
        self.assertIsInstance(t, Task)

    def test_description_as_string(self):
        t = Task('a')
        self.assertEqual(t.description, 'a')

    def test_plan(self):
        t = Task()
        d = datetime.date(2018,12,1)
        t.convert_to_plan(d)

    def test_plan_as_tuple(self):
        t = Task()
        t.convert_to_plan((2018,12,1))
        self.assertEqual(t.plan_date.month, 12)
