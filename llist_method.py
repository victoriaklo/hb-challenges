# Here’s a snippet from a linked list class:

# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
# Write a method for this class called print_nodes. It should print out the data for each node in the linked list and return None.

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def print_nodes(self):
        curr = self.head
        while curr is not None:
            print(curr.data)

            curr = curr.next