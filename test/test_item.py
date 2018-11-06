from unittest import TestCase

from tiger.item import Item

class TestItem(TestCase):

    def test_item(self):
        t = Item()
        self.assertIsInstance(t, Item)
