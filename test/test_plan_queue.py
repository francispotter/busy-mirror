from unittest import TestCase
import datetime

from tiger.queue import PlanQueue
from tiger.item import Plan

class TestPlanQueue(TestCase):

    def test_plan_queue(self):
        q = PlanQueue()
        d1 = datetime.date(2018,12,5)
        q.add(Plan(d1, 'a'))
        d2 = datetime.date(2018,12,6)
        q.add(Plan(d2, 'b'))
        p = q.get()
        self.assertEqual(p.date.day, 5)
