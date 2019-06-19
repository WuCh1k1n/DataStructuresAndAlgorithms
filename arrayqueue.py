from arrays import Array


class ArrayQueue(Array):
    """An array-based queue implementation."""
    DEFAULT_CAPACITY = 10  # For all array queue

    def __init__(self, sourceCollection=None):
        """Sets the initial state of self, which includes the
        content of sourceCollection, if it's present."""
        self._items = Array(ArrayStack.DEFAULT_CAPACITY)
        self._front = self._items[0]
        self._rear = self._items[0]
        AbstractStack.__init__(self, sourceCollection)

    # Accessor methods

    def __iter__(self):
        """Supports iteration over a view of self.
        Visits items from front to rear of queue."""
        cursor = self._front
        if self._front <= self._rear:
            while cursor <= self._rear:
                yield self._items[cursor]
                cursor += 1
        else:
            while cursor < len(self._items) - 1:
                yield self._items[cursor]
                cursor += 1
            cursor = 0
            while cursor <= self._rear:
                yield self._items[cursor]
                cursor += 1

    def peek(self):
        """Returns the item at front of the queue.
        Precondition: the queue is not empty.
        Raise KeyError if the queue is empty."""
        if self.isEmpty():
            raise KeyError("The queue is empty.")
        return self._front

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self._size = 0
        self._items = Array(ArrayStack.DEFAULT_CAPACITY)
        self._front = self._items[0]
        self._rear = self._items[0]

    def add(self, item):
        """Adds item to the rear of the queue."""
        if self.isEmpty():
            self._items[self._front] = item
        elif len(self) == len(self._items):  # The logical size of array equals the physical size
            newArray = Array(ArrayStack.DEFAULT_CAPACITY * 2)
            cursor = self._front
            newCursor = 0
            while cursor < len(self._items):
                newArray[newCursor] = self._items[cursor]
                cursor += 1
                newCursor += 1
            cursor = 0
            while cursor <= self._rear:
                newArray[newCursor] = self._items[cursor]
                cursor += 1
                newCursor += 1
            newArray[newCursor] = item
            self._items = newArray
        else:
            if self._rear == len(self._items) - 1:  # The item at rear of queue is the last item of array
                self._rear = 0
            else:
                self._rear += 1
            self._items[self._rear] = item
        self._size += 1

    def pop(self):
        """Removes and returns the item at front of the queue.
        Precondition: the queue is not empty.
        Raise KeyError if the queue is empty.
        Postcondition: the front item is removed from the queue."""
        if self.isEmpty():
            raise KeyError("The queue is empty.")
        oldItem = self._items[self._front]
        if self._front == self._rear:  # Only one item in the queue
            self._front, self_rear = 0
        elif self._front == len(self._items) - 1:  # The item at front of queue is the last item of array
            self._front = 0
        else:
            self._front += 1
        self._size -= 1
        # Resize array here if necessary
        return oldItem
