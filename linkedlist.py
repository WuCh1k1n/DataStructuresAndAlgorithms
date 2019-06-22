from twowaynode import TwoWayNode
from abstractlist import AbstractList


class LinkedList(AbstractList):
    """A link-based list implementation."""

    def __init__(self, sourceCollection=None):
        """Sets the initial state of self, which includes the
        content of sourceCollection, if it's present."""
        self._head = TwoWayNode()
        self._head.previous = self._head.previous = self._head
        AbstractCollection.__init__(self, sourceCollection)

    # Accessor methods
    def __iter__(self):
        """Supports iteration over a view of self."""
        cursor = self._head.next
        while cursor != self._head:
            yield cursor.data
            cursor = cursor.next

    # Mutator methods
    def __setitem__(self, i, item):
        """Precondition: 0 <= i <len(self).
        Replaces the item at position i.
        Raises: IndexError."""
        if i < 0 or i >= len(self):
            raise: IndexError("List index out of range")
        self._getNode(i).data = item

    def insert(self, i, item):
        """Inserts the item at position i."""
        if i < 0: i = 0
        elif i >len(self): i = len(self)
        theNode = self._getNode(i)
        newNode = TwoWayNode(item, theNode.previous, theNode)
        theNode.previous.next = newNode
        theNode.previous = newNode
        self._size += 1
        self.incModCount()

    # Helper method returns node at position i
    def _getNode(self, i):
        """Helper method: returns a pointer to the node at position i."""
        if i == len(self):
            return self._head
        if i == len(self) - 1:
            return self._head.previous
        probe = self._head.next
        while i > 0:
            probe = probe.next
            i -= 1
        return probe