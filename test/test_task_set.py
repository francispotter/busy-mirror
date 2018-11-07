from unittest import TestCase
import datetime

from tiger.task_set import TaskSet
from tiger.task import Task

class TestTaskSet(TestCase):

    def test_get(self):
        q = TaskSet()
        q.add_todo(Task('a'))
        t = q.get_todo()
        self.assertEqual(str(t),'a')

    # def test_list(self):
    #     q = TaskSet()
    #     q.todo.add(Task('a'))
    #     q.todo.add(Task('b'))
    #     s = q.todo.list()
    #     self.assertEqual(len(s), 2)
    #     self.assertEqual(s[1][0], 2)
    #     self.assertEqual(str(s[0][1]), 'a')
    #     self.assertIsInstance(s[1][1], Task)
    #
    # def test_defer(self):
    #     q = TaskSet()
    #     q.todo.add(Task('a'))
    #     d = datetime.date(2018,12,25)
    #     q.defer(d)
    #     self.assertEqual(q.plan.get().date.year, 2018)
