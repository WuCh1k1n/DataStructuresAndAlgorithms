class BagInterface(object):
    """Interface for all bag types."""

    # Constructor
    def __init__(self, sourceCollection=None):
        """Sets the initial state of self, which includes the
        content of sourceCollection, if it's present."""
        pass

    # Accessor method
    def isEmpty(self):
        """Return True if len(self) ==0,
        or False otherwise."""
        return True

    def __len__(self):
        """Return the number of items in self."""
        return 0

    def __iter__(self):
        """Supports iteration over a view of self."""
        return None

    def __add__(self, other):
        """Return a new bag containing the contents
        of self and other."""
        return None

    def __eq__(self, other):
        """Return True if self equals other,
        or False otherwise."""
        return False

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        pass

    def add(self, item):
        """add item to self."""
        pass

    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item in not in self.
        Postcondition: item is removed from self."""
        pass
