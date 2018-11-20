from unittest import TestCase
from pathlib import Path
from tempfile import TemporaryDirectory

from todo.queue_file import QueueFile
from todo.queue import Queue
from todo.task import Task
from todo.task import TODO_SCHEMA
from todo.task import PLAN_SCHEMA

class TestQueueFile(TestCase):

    def test_load_tasks(self):
        p = Path(__file__).parent.joinpath('test_tasks.txt')
        f = QueueFile(p, Task, TODO_SCHEMA)
        q = f.queue
        self.assertIsInstance(q, Queue)
        self.assertEqual(str(q.get()), 'a')
        self.assertIsInstance(q.get(), Task)

    def test_load_if_not_there(self):
        p = Path(__file__).parent.joinpath('not_there.txt')
        f = QueueFile(p, Task, TODO_SCHEMA)
        q = f.queue
        self.assertIsInstance(q, Queue)
        self.assertEqual(q.count(), 0)

    def test_save_tasks(self):
        with TemporaryDirectory() as d:
            p = Path(d) / 'todo.txt'
            f1 = QueueFile(p, Task, TODO_SCHEMA)
            q1 = f1.queue
            q1.add(Task('a'))
            f1.save()
            f2 = QueueFile(p, Task, TODO_SCHEMA)
            q2 = f2.queue
            self.assertEqual(str(q2.get()), 'a')

    def test_plan_file(self):
        with TemporaryDirectory() as d:
            p = Path(d) / 'plan.txt'
            f = QueueFile(p, Task, PLAN_SCHEMA)
            t = Task('a').as_plan((2019,2,3))
            f.queue.add(t)
            f.save()
            q2 = QueueFile(p, Task, PLAN_SCHEMA).queue
            self.assertEqual(q2.get().plan_date.day, 3)
