'''
A queue is unaware of the classes of its contents
Method calls on queue use indices that start at 1
'''


from .selector import Selector

class Queue:

    def __init__(self, *items):
        self._items = items or []

    def all(self):
        return self._items

    def count(self):
        return len(self._items)

    def add(self, *items):
        for item in items:
            self._items.append(item)

    def get(self, index=1):
        return self._items[index-1] if self._items else None

    def select(self, *criteria):
        selector = Selector(criteria)
        return selector.indices([str(i) for i in self._items])

    def _split(self, *criteria):
        indices = self.select(*criteria)
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

    def list(self, *criteria):
        return [(i+1, self._items[i]) for i in self.select(*criteria)]

    def remove(self, items):
        if isinstance(items, list):
            for item in items:
                self._items.remove(item)
        else:
            self._items.remove(items)
