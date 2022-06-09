# Given a node class:
class Node(object):
    """Linked list node."""

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def as_rev_string(self):
        """Represent data for this node and its successors as a string.

        >>> l1 = Node(3)
        >>> l1.as_rev_string()
        '3'

        >>> l1 = Node(3, Node(2, Node(1)))
        >>> l1.as_rev_string()
        '123'
        """

        out = []
        n = self

        while n:
            out.append(str(n.data))
            n = n.next

        return "".join(reversed(out))

# Directions:
# You will be given two linked lists in “reverse-digit” format: 123 and 456
# You should sum up these numbers and return the sum of these two numbers in the same “reverse-digit” format.
# For 123 + 456, this should return 579. 

def add_linked_lists(l1, l2):
    """Given two linked lists, treat like numbers and add together.

    l1: the head node of a linked list in "reverse-digit" format
    l2: the head node of another "reverse-digit" format

    Returns: head node of linked list of sum in "reverse-digit" format.
    """
