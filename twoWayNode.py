class TwoWayNode(object):

    def __init__(self, data, previous=None, next=None):
        """Instantiates a TwoWayNode."""
        self.data = data
        self.previous = previous
        self.next = next