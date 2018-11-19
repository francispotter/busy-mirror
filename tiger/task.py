from datetime import date as Date
from datetime import datetime as DateTime

TODO_STATE = 't'
PLAN_STATE = 'p'
DONE_STATE = 'd'

TODO_SCHEMA = ['description']

PLAN_SCHEMA = ['description', 'plan_date']

class Task:

    def __init__(self, description=None, plan_date=None):
        assert isinstance(description, str)
        assert description
        self._description = description
        self._state = TODO_STATE
        if plan_date: self.as_plan(plan_date)

    def __str__(self):
        return self._description

    @property
    def description(self):
        return self._description

    def as_plan(self, date):
        self._state = PLAN_STATE
        if isinstance(date, Date):
            self._plan_date = date
        elif isinstance(date, tuple):
            self._plan_date = Date(*date)
        elif isinstance(date, str):
            self._plan_date = DateTime.strptime(date, '%Y-%m-%d').date()
        else:
            raise RuntimeError("Plan requires a date")
        return self


    @property
    def plan_date(self):
        return self._plan_date
