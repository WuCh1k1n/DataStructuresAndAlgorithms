from abstractcollection import AbstractCollection


class AbstractQueue(AbstractCollection):
    """An abstract queue implementation."""

    # Constructor
    def __init__(self, sourceCollection=None):
        """Sets the initial state of self, which includes the
        content of sourceCollection, if it's present."""
        AbstractCollection(self, sourceCollection)
