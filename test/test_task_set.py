from unittest import TestCase
import datetime

from tiger.system import System
from tiger.task import Task

class TestSystem(TestCase):

    def test_get(self):
        q = System()
        q.add(Task('a'))
        t = q.get()
        self.assertEqual(str(t),'a')

    def test_list(self):
        s = System()
        s.add(Task('a'))
        s.add(Task('b'))
        i = s.list()
        self.assertEqual(len(i), 2)
        self.assertEqual(i[1][0], 2)
        self.assertEqual(str(i[0][1]), 'a')
        self.assertIsInstance(i[1][1], Task)

    def test_defer(self):
        s = System()
        s.add(Task('a'))
        d = datetime.date(2018,12,25)
        s.defer(d)
        self.assertEqual(s.get('plan').plan_date.year, 2018)

    def test_pop(self):
        s = System()
        t1 = Task('a')
        t2 = Task('b')
        s.add(t1)
        s.add(t2)
        s.pop()
        i = s.list()
        self.assertEqual(len(i), 2)
        self.assertEqual(str(i[0][1]), 'b')

    def test_by_number(self):
        s = System()
        s.add(Task('a'))
        s.add(Task('b'))
        t = s.get(criteria=2)
        self.assertEqual(str(t), 'b')

    def test_create_with_string(self):
        s = System()
        s.add('a')
        self.assertEqual(str(s.get()), 'a')

    def test_create_with_multiple_strings(self):
        s = System('a','b','c')
        self.assertEqual(str(s.get(criteria=2)), 'b')

    def test_select_multiple(self):
        s = System('a','b','c')
        t = s.select(1,3)
        self.assertEqual(len(t), 2)
