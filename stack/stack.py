"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order.

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when
   implementing a Stack?
"""


class Stack:
    def __init__(self):
        self.storage = []

    def __len__(self):
        return len(self.storage)

    def push(self, value):
        self.storage.append(value)

    def pop(self):
        if len(self.storage) > 0:
            return self.storage.pop()

# class Node:

#     # Class to create nodes of linked list
#     # constructor initializes node automatically
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# class Stack:
#     def __init__(self):
#         self.head = None
#         self.size = 0
#         # self.storage = []

#     def __len__(self):
#         return self.size

#     def push(self, value):
#         if self.head == None:
#             self.head = Node(value)

#         else:
#             newnode = Node(value)
#             newnode.next = self.head
#             self.head = newnode
#         self.size += 1

#     def pop(self):
#         if self.size == 0:
#             return None
#         else:
#             popped = self.head.data
#             self.head = self.head.next
#             self.size -= 1
#             return popped

