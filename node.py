class Node(object):
    """Represents a singly linked node."""

    def __init__(self, data, next = None):
        """Instantiates a Node with a default next of None."""
        self.data = data
        self.next = next


def travelsal(head):
    probe = head
    while probe.next != None:
        probe = probe.next


def search(head, targetItem):
    probe = head
    while probe.next != None and targetItem != probe.data:
        probe = probe.next
    if probe != None:
        return probe
    else:
        return None


def replaceTargetNode(head, targetItem, newItem):
    probe = head
    while probe.next != None and targetItem != probe.data:
        probe = probe.next
    if probe != None:
        probe.data = newItem
        return True
    else:
        return False


def replaceIndexNode(head, index, newItem):
    probe = head
    while index > 0:
        probe = probe.next
        index -= 1
    probe.data = newItem


def insert(head, index, newItem):
    if head is None or index <= 0:
        head = Node(newItem, head)
    else:
        probe = head
        while index > 1 and probe.next != None:
            probe = probe.next
            index -= 1
        probe.next = Node(newItem, probe.next)


def remove(head, index):
    if index <= 0 or head.next is None:
        removeItem = head.data
        head = head.next
        return removeItem
    else:
        probe = head
        while index > 1 and probe.next != None:
            probe = probe.next
            index -= 1
        removeItem = probe.next.data
        probe.next = probe.next.next
        return removeItem
