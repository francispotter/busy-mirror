from unittest import TestCase

from tiger.queue import Queue

class TestQueue(TestCase):

    def test_list(self):
        q = Queue()
        q.add('a')
        q.add('b')
        i = q.list()
        self.assertEqual(i[0], (1, 'a'))

    def test_list_with_criteria(self):
        q = Queue('a','b','c')
        i = q.list(1,3)
        self.assertEqual(i[1], (3, 'c'))

    def test_select_multiple(self):
        q = Queue('a','b','c')
        t = q.select(1,3)
        self.assertEqual(len(t), 2)

    def test_pop_multiple(self):
        q = Queue('a','b','c','d')
        q.pop(2,4)
        self.assertEqual(str(q.get(2)), 'd')

    def test_pop_if_nothing(self):
        q = Queue()
        q.pop()
        self.assertEqual(q.count(), 0)

    def test_drop(self):
        q = Queue('a','b','c','d')
        q.drop()
        self.assertEqual(str(q.get(1)), 'b')

    def test_delete(self):
        q = Queue('a','b','c')
        q.delete(2,3)
        self.assertEqual(q.count(), 1)
