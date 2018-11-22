from unittest import TestCase
from pathlib import Path
from tempfile import TemporaryDirectory

from todo.file import TodoFile
from todo.file import PlanFile
from todo.queue import Queue
from todo.task import Task

class TestFile(TestCase):

    def test_load_tasks(self):
        p = Path(__file__).parent.joinpath('test_tasks.txt')
        f = TodoFile(p)
        q = f.queue
        self.assertIsInstance(q, Queue)
        self.assertEqual(str(q.get()), 'a')
        self.assertIsInstance(q.get(), Task)

    def test_load_if_not_there(self):
        p = Path(__file__).parent.joinpath('not_there.txt')
        f = TodoFile(p)
        q = f.queue
        self.assertIsInstance(q, Queue)
        self.assertEqual(q.count(), 0)

    def test_save_tasks(self):
        with TemporaryDirectory() as d:
            p = Path(d) / 'todo.txt'
            f1 = TodoFile(p)
            q1 = f1.queue
            q1.add(Task('a'))
            f1.save()
            f2 = TodoFile(p)
            q2 = f2.queue
            self.assertEqual(str(q2.get()), 'a')

    def test_plan_file(self):
        with TemporaryDirectory() as d:
            p = Path(d) / 'plan.txt'
            f = PlanFile(p)
            t = Task('a').as_plan((2019,2,3))
            f.queue.add(t)
            f.save()
            q2 = PlanFile(p).queue
            self.assertEqual(q2.get().plan_date.day, 3)
