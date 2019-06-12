class AbstractCollection(object):
    """An abstract collection implementation."""

    # Constructor
    def __init__(self, sourceCollection=None):
        """Sets the initial state of self, which includes the
        content of sourceCollection, if it's present."""
        self._size = 0
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)

    # Accessor methods
    def __str__(self):
        """Return the string representation of self."""
        return "[" + ",".join(map(self)) + "]"

    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise."""
        if self is other:
            return True
        if type(self) != type(other) or len(self) != len(other):
            return False
        otherIter = iter(other)
        for item in self:
            if item != next(otherIter):
                return False
        return True
