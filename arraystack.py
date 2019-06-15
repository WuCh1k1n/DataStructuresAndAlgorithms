from arrays import Array
from abstractstack import AbstractStack


class ArrayStack(AbstractStack):
    """An array-based stack implementation."""
    DEFAULT_CAPACITY = 10  # For all array stacks

    def __init__(self, sourceCollection=None):
        """Sets the initial state of self, which includes the
        content of sourceCollection, if it's present."""
        self._items = Array(ArrayStack.DEFAULT_CAPACITY)
        AbstractStack.__init__(self, sourceCollection)

    # Accessor methods 
    def __iter__(self):
        """Supports iteration over a view of self.
        Visits items from bottom to top of stack."""
        cursor = 0
        while cursor < len(self._items):
            yield self._items[cursor]
            cursor += 1

    def peek(self):
        """Returns the item at top of the stack.
        Precondition: the stack is not empty.
        Raise KeyError if the stack is empty."""
        if isEmpty(self):
            raise KeyError("the stack is empty")
        return self._items[len(self) - 1]

    # Mutator mehtods
    def clear(self):
        """Makes self become empty."""
        self._size = 0
        self._items = Array(ArrayStack.DEFAULT_CAPACITY)

    def push(self, item):
        """Insert item at top of the stack."""
        # Resize array here if necessary
        self._items[len(self)] = item
        self._size += 1

    def pop(self):
        """Removes and returns the item at top of the stack.
        Precondition: the stack is not empty.
        Raise KeyError if the stack is empty.
        Postcondition: the top item is removed from the stack."""
        if isEmpty(self):
            raise KeyError("the stack is empty")
        oldItem = self._items[len(self)]
        self._size -= 1
        # Resize array here if necessary
        return oldItem
