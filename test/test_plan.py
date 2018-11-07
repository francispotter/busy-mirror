from unittest import TestCase
import datetime

from tiger.task import Plan
from tiger.task import Task

class TestPlan(TestCase):

    def test_plan(self):
        d = datetime.date(2018,11,6)
        p = Plan(d, 'v')
        self.assertEqual(p.date.month, 11)
        self.assertIsInstance(p.task, Task)
