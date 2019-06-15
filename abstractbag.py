from abstractcollection import AbstractCollection


class AbstractBag(AbstractCollection):
    """An abstract bag implementation."""

    # Constructor
    def __init__(self, sourceCollection=None):
        """Sets the initial state of self, which includes the
        content of sourceCollection, if it's present."""
        AbstractCollection(self, sourceCollection)
