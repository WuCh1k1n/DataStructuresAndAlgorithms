"""
File: arrays.py

An Array is like a list, but the client can use
only [], len, iter, and str.

To instantiate, use

<variable> = Array(<capacity>, <optional fill value>)

The fill value is None by default.
"""


class Array(object):
    """Represents an array."""

    def __init__(self, capacity, fillValue = None):
        """Capacity is the static size of the array.
        fillValue is placed at each position"""
        self._items = list()
        self.defaultCapacity = capacity
        self.logicalSize = 0
        for count in range(capacity):
            self._items.append(fillValue)
    
    def __len__(self):
        """-> The capacity of the array."""
        return len(self._items)

    def __str__(self):
        """-> The string representation of the array."""
        return str(self._items)

    def __iter__(self):
        """Supports traversal with a for loop."""
        return iter(self._items)

    def __getitem__(self, index):
        """Subscript operator for access at index."""
        return self._items[index]

    def __setitem__(self, index, newItem):
        self._items[index] = newItem


class ArrayHelper(object):
    """A helper to operate an array."""

    def increase(self, array):
        """Increase the physical size of array."""
        temp = Array(len(array) * 2)
        temp.logicalSize = array.logicalSize
        temp.defaultCapacity = array.defaultCapacity
        for i in range(array.logicalSize):
            temp[i] = array[i]
        array = temp
        return array

    def decrease(self, array):
        """Decrease the physical size of array."""
        temp = Array(len(self._array) // 2)
        temp.logicalSize = array.logicalSize
        temp.defaultCapacity = array.defaultCapacity
        for i in range(array.logicalSize):
            temp[i] = array[i]
        array = temp
        return array

    def insert(self, array, targetIndex, newItem):
        """Insert a element into particular position of array."""
        if array.logicalSize == len(array):
            array = self.increase(array)
        for i in range(array.logicalSize, targetIndex, -1):
            array[i] = array[i - 1]
        array[targetIndex] = newItem
        array.logicalSize += 1
        return array

    def delete(self, array, targetIndex):
        """Delete a particular element of array."""
        for i in range(targetIndex, array.logicalSize):
            array[i] = array[i + 1]
        array.logicalSize -= 1
        if array.logicalSize <= len(array) // 4 and len(array) >= array.defaultCapacity * 2:
            array = self.decrease(array)
        return array
