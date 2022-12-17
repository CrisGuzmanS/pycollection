class Collection:
    def __init__(self, items: list):
        self._items = items
        self._index = 0

    def __iter__(self):
        self._index = -1
        return self

    def count(self):
        return len(self._items)

    def find(self, index:int):
        return self.item(self._items[index])

    def item(self, item):
      return item

    def first(self):
        return self.item(self._items[0])

    def append(self, element):
        self._items.append(element)

    def items(self):
        return self._items

    def __next__(self):
        self._index += 1
    
        if self._index <= len(self._items):
            return self.item(self._items[self._index])
            
        self._index = -1
        
        raise StopIteration