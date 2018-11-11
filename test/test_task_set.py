from unittest import TestCase
import datetime

from tiger.task_set import TaskSet
from tiger.task import Task

class TestTaskSet(TestCase):

    def test_get(self):
        q = TaskSet()
        q.add(Task('a'))
        t = q.get()
        self.assertEqual(str(t),'a')

    def test_list(self):
        s = TaskSet()
        s.add(Task('a'))
        s.add(Task('b'))
        i = s.list()
        self.assertEqual(len(i), 2)
        self.assertEqual(i[1][0], 2)
        self.assertEqual(str(i[0][1]), 'a')
        self.assertIsInstance(i[1][1], Task)

    def test_defer(self):
        s = TaskSet()
        s.add(Task('a'))
        d = datetime.date(2018,12,25)
        s.defer(d)
        self.assertEqual(s.get('plan').plan_date.year, 2018)
