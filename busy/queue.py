# Method calls on queue use indices that start at 1

from .selector import Selector
from .item import Task

class Queue:

    schema = ['description']
    listfmt = "{1.description}"

    def __init__(self, *items):
        self._items = []
        self.add(*items)

    def all(self):
        return self._items

    def count(self):
        return len(self._items)


    # Add new tasks. Always makes them tasks. Also does inserts.

    def add(self, *items, index=None):
        newtasks = [Task.create(i) for i in items if i]
        index = len(self._items) if index == None else index
        self._items[index:index] = newtasks


    # Replace existing tasks at the indices provided. Also inserts if the
    # indices run out. Does not create tasks. Would be good to combine this
    # with the add method.

    def replace(self, indices, newvalues):
        while newvalues and indices:
            self._items[indices.pop(0)] = newvalues.pop(0)
        while indices:
            del self._items[indices.pop()]
        self._items.extend(newvalues)


    def get(self, index=1):
        return self._items[index-1] if self._items else None

    def select(self, *criteria):
        selector = Selector(criteria)
        return selector.indices(self._items)

    def _split(self, *criteria):
        return self._split_by_indices(*self.select(*criteria))

    def _split_by_indices(self, *indices):
        inlist = [t for i,t in enumerate(self._items) if i in indices]
        outlist = [t for i,t in enumerate(self._items) if i not in indices]
        return (inlist, outlist)

    def pop(self, *criteria):
        hilist, lolist = self._split(*criteria or [len(self._items)])
        self._items = hilist + lolist
        return hilist

    def drop(self, *criteria):
        lolist, hilist = self._split(*criteria or [1])
        self._items = hilist + lolist
        return lolist

    def delete(self, *criteria):
        killlist, keeplist = self._split(*criteria)
        self._items = keeplist
        return killlist

    def delete_by_indices(self, *indices):
        killlist, keeplist = self._split_by_indices(*indices)
        self._items = keeplist
        return killlist

    def list(self, *criteria):
        return [(i+1, self._items[i]) for i in self.select(*criteria)]

    @property
    def strings(self):
        return [str(i) for i in self._items]

class TodoQueue(Queue):
    pass

class PlanQueue(Queue):
    schema = ['plan_date', 'description']
    listfmt = "{1.plan_date:%Y-%m-%d}  {1.description}"
