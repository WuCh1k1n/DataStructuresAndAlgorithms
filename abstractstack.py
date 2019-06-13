from abstractcollection import AbstractCollection


class AbstractStack(AbstractCollection):
    """An abstract stack implementation."""

    # Constructor
    def __init__(self, sourceCollection=None):
        """Sets the initial state of self, which includes the
        content of sourceCollection, if it's present."""
        AbstractCollection(self, sourceCollection)

    # Mutator methods
    def add(self, item):
        """Adds item to self."""
        self.push(item)