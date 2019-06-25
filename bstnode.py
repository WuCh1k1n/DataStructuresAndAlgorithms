class BSTNode(object):
    """Represents a singly binary search tree node."""

    def __init__(self, data, left=None, right=None):
        """Instantiates a Node with default left of None and default right of None."""
        self.data = data
        self.left = left
        self.right = right
