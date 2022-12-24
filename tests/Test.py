import unittest
from test import support
from pycollection import Collection

class Number:

    def __init__(self, item):
        self._item = item

    def equals(self, number:int):
        return self._item == number

    def value(self):
        return self._item


class NumberCollection(Collection):
    def item(self, item):
        return Number(item)

class MyTestCase(unittest.TestCase):

    def test_random_method(self):
        numbers = NumberCollection([1,2,3,4,5,6,7,8])
        self.assertGreater(numbers.random().value(), 0)

    def test_where_method(self):
        numbers = NumberCollection([1,2,3,4,5])
        assert numbers.where(is_more_than_3).count() == 2

def is_more_than_3(element):
    return element.value() > 3

if __name__ == '__main__':
    unittest.main()