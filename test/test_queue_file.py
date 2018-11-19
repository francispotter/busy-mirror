from unittest import TestCase
from pathlib import Path
from tempfile import TemporaryDirectory

from tiger.queue_file import QueueFile
from tiger.queue import Queue
from tiger.task import Task
from tiger.task import TODO_SCHEMA
from tiger.task import PLAN_SCHEMA

class TestQueueFile(TestCase):

    def test_load_tasks(self):
        p = Path(__file__).parent.joinpath('test_tasks.txt')
        f = QueueFile(p, Task, TODO_SCHEMA)
        q = f.load()
        self.assertIsInstance(q, Queue)
        self.assertEqual(str(q.get()), 'a')
        self.assertIsInstance(q.get(), Task)

    def test_load_if_not_there(self):
        p = Path(__file__).parent.joinpath('not_there.txt')
        f = QueueFile(p, Task, TODO_SCHEMA)
        q = f.load()
        self.assertIsInstance(q, Queue)
        self.assertEqual(q.count(), 0)

    def test_save_tasks(self):
        with TemporaryDirectory() as d:
            p = Path(d) / 'todo.txt'
            q1 = Queue(Task('a'))
            f = QueueFile(p, Task, TODO_SCHEMA)
            f.save(q1)
            q2 = f.load()
            self.assertEqual(str(q2.get()), 'a')

    def test_plan_file(self):
        with TemporaryDirectory() as d:
            p = Path(d) / 'plan.txt'
            t = Task('a').as_plan((2019,2,3))
            q1 = Queue(t)
            f = QueueFile(p, Task, PLAN_SCHEMA)
            f.save(q1)
            q2 = f.load()
            self.assertEqual(q2.get().plan_date.day, 3)
