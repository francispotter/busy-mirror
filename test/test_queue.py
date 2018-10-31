from unittest import TestCase

from tiger2.queue import Queue

class TestQueue(TestCase):

    def test_list(self):
        q = Queue()
        q.add('a')
        q.add('b')
        i = q.list()
        self.assertEqual(i[0], (1, 'a'))
