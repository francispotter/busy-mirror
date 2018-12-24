from unittest import TestCase
import datetime

from busy.item import Task


class TestTask(TestCase):

    def test_task(self):
        t = Task('b')
        self.assertIsInstance(t, Task)

    def test_description_as_string(self):
        t = Task('a')
        self.assertEqual(t.description, 'a')

    def test_task_requires_description(self):
        with self.assertRaises(AssertionError):
            t = Task('')

    def test_plan(self):
        t = Task('a')
        d = datetime.date(2018,12,1)
        t.as_plan(d)

    def test_plan_as_tuple(self):
        t = Task('b')
        t.as_plan((2018,12,1))
        self.assertEqual(t.plan_date.month, 12)

    def test_plan_requires_date(self):
        t = Task('c')
        with self.assertRaises(RuntimeError):
            t.as_plan(54)

    def test_plan_with_date_as_string(self):
        t = Task ('d')
        t.as_plan('2019-04-05')
        self.assertEqual(t.plan_date.day, 5)

    def test_create_task_with_dict(self):
        t = Task(plan_date=(2019,4,15), description='a')
        self.assertEqual(t.plan_date.month, 4)

    def test_tags(self):
        t = Task('f #a')
        self.assertEqual(t.tags, ['a'])

    def test_project(self):
        t = Task("k #oNe #two")
        self.assertEqual(t.project, 'one')
