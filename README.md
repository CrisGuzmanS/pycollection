# pycollection

pycollection is an amazing library that allows you to iterate through a list, but it returns a transformed item. It has a lot of methods to interact with the collection. It works similar than laravel collections.

## Instalation

`pip install pycollection`

## Basic usage
    
    from pycollection import collection

    class NumberCollection(Collection):

        def item(self, item):
            return Number(item)


    class Number:

        def __init__(self, item):
            self._item = item

        def value(self):
            return self._item
        
        def squared(self):
            return self._item * self._item


    numbers = NumberCollection([1,2,3,4,5])


    for number in numbers:
        print(number.squared())

    # output
    # > 1
    # > 4
    # > 9
    # > 16
    # > 25

As you can see, it allows for an easy-to-read syntax for navigating between lists and their elements, since you can provide new functionality to both.

## Available methods

| methods                        | action                                                    |
|----------------------------| -------------------------------------------------- |
| count()                          | gets the number of total elements in the list  |
| json()                            | jsonifies the list                                     |
| find(callaback: Callable)  | returns the first item that match with the callback |
| where(callback: Callable) | returns a new collection that meets the callback |
| item(element)    | transforms each of the elements of the list when it is iterated over it |
| first()                           | gets the first item of the list                      |
| append(element)             | add a new element to the list                        |
| items()                  | retrieves the collection list |
| random()                      | retrieves a random item from the collection      |
| get(index:int)                | retrieves an element according to the given index |