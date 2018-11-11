from datetime import date as Date

TODO_STATE = 't'
PLAN_STATE = 'p'
DONE_STATE = 'd'

class Task:

    def __init__(self, description):
        if not description:
            raise RuntimeError("Task requires a description")
        self._description = description
        self._state = TODO_STATE
        self._plan_date = None

    def __str__(self):
        return self._description

    @property
    def description(self):
        return self._description

    def convert_to_plan(self, date):
        self._state = PLAN_STATE
        if isinstance(date, Date):
            self._plan_date = date
        elif isinstance(date, tuple):
            self._plan_date = Date(*date)
        else:
            raise RuntimeError("Plan requires a date")


    @property
    def plan_date(self):
        return self._plan_date
