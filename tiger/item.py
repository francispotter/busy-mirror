class Item:
    pass

class Task(Item):

    def __init__(self, description):
        self._description = description

    def __str__(self):
        return self._description

class Plan(Item):

    def __init__(self, date, task):
        self._date = date
        if isinstance(task, Task):
            self._task = task
        else:
            self._task = Task(task)

    @property
    def date(self):
        return self._date

    @property
    def task(self):
        return self._task
