from abstractcollection import AbstractCollection


class AbstractBag(AbstractCollection):
    """An abstract bag implementation."""

    # Constructor
    def __init__(self, sourceCollection=None):
        """Sets the initial state of self, which includes the
        content of sourceCollection, if it's present."""
        AbstractCollection(self, sourceCollection)

    # Accessor methods
    def isEmpty(self):
        """Returns True if len(self) == 0, or False otherwise."""
        return len(self) == 0

    def __len__(self):
        """Returns the number of items in self."""
        return self._size

    def __str__(self):
        """Return the string representation of self."""
        return "{" + ",".join(map(self)) + "}"

    def __add__(self, other):
        """Returns a new bag containing the contents
        of self and other."""
        result = type(self)(self)
        for item in other:
            result.add(item)
        return result
