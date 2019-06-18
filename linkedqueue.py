from node import Node
from abstractqueue import AbstractQueue


class LinkedQueue(AbstractQueue):

    def __init__(self, sourceCollection=None):
        """Sets the initial state of self, which includes the
        content of sourceCollection, if it's present."""
        self._front = None
        self._rear = None
        AbstractStack.__init__(self, sourceCollection)


    # Accessor methods
    def __iter__(self):
        """Supports iteration over a view of self.
        Visits items from front to rear of queue."""
        def visitNodes(node):
            if not node is None:
                tempList.append(node.data)
                visitNodes(node.next)
        tempList = list()
        visitNodes(self._front)
        return iter(tempList)
    
    def peek(self):
        """Returns the item at front of the queue.
        Precondition: the queue is not empty.
        Raise KeyError if the queue is empty."""
        if self.isEmpty():
            raise KeyError("The queue is empty.")
        return self._front.data

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self._size = 0
        self._front = None
        self._rear = None

    def add(self, item):
        """Adds item to the rear of the queue."""
        newNode = Node(item, None)
        if self.isEmpty():
            self._front = newNode
        else:
            self._rear.next = newNode
        self._rear = newNode
        self._size += 1

    def pop(self):
        """Removes and returns the item at front of the queue.
        Precondition: the queue is not empty.
        Raise KeyError if the queue is empty.
        Postcondition: the front item is removed from the queue."""
        if self.isEmpty():
            raise KeyError("The queue is empty.")
        oldItem = self._front.data
        self._front = self._front.next
        if self._front is None:
            self._rear = None
        self._size -= 1
        return oldItem
