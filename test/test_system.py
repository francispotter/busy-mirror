from unittest import TestCase
import datetime

from busy.system import System
from busy.task import Task

class TestSystem(TestCase):

    def test_get(self):
        q = System()
        q.add_todos(Task('a'))
        t = q.get_todo()
        self.assertEqual(str(t),'a')

    def test_list(self):
        s = System()
        s.add_todos(Task('a'))
        s.add_todos(Task('b'))
        i, m = s.list()
        self.assertEqual(len(i), 2)
        self.assertEqual(i[1][0], 2)
        self.assertEqual(str(i[0][1]), 'a')
        self.assertIsInstance(i[1][1], Task)

    def test_defer(self):
        s = System()
        s.add_todos(Task('a'))
        d = datetime.date(2018,12,25)
        s.defer(d)
        self.assertEqual(s.count_plans(), 1)
        self.assertEqual(s.get_plan(1).plan_date.year, 2018)

    def test_pop(self):
        s = System()
        t1 = Task('a')
        t2 = Task('b')
        s.add_todos(t1)
        s.add_todos(t2)
        s.pop()
        i, m = s.list()
        self.assertEqual(len(i), 2)
        self.assertEqual(str(i[0][1]), 'b')

    def test_by_number(self):
        s = System()
        s.add_todos(Task('a'))
        s.add_todos(Task('b'))
        t = s.get_todo(2)
        self.assertEqual(str(t), 'b')

    def test_create_with_string(self):
        s = System()
        s.add_todos('a')
        self.assertEqual(str(s.get_todo()), 'a')
        self.assertIsInstance(s.get_todo(), Task)

    def test_create_with_multiple_strings(self):
        s = System('a','b','c')
        self.assertIsInstance(s.get_todo(), Task)
        self.assertEqual(s.count_todos(), 3)
        self.assertEqual(str(s.get_todo(2)), 'b')

    def test_select_multiple(self):
        s = System('a','b','c')
        t = s.select(1,3)
        self.assertEqual(len(t), 2)

    def test_list_plans(self):
        s = System('a','b')
        s.defer((2018,12,4))
        self.assertEqual(s.count_plans(), 1)

    def test_defer_by_index(self):
        s = System('a','b')
        s.defer((2018,12,4),2)
        t = s.get_todo()
        self.assertEqual(s.count_plans(),1)
        self.assertEqual(str(t), 'a')

    def test_defer_multiple(self):
        s = System('a','b','c')
        s.defer((2018,12,5),1,3)
        p = s.get_plan(2)
        self.assertEqual(str(p), 'c')
