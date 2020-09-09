"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return len(self.storage)

    def enqueue(self, value):
        self.storage.insert(0,value)

    def dequeue(self):
        if self.storage != []:
         return self.storage.pop()



# A class to represent a queue

# The queue, front stores the front node
# of LL and rear stores the last node of LL

# class Node:

#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next


# class Queue:

#     def __init__(self):
#         self.head = None  
#         self.tail = None
#         self.length = 0

#     def __len__(self):
#         return self.length

#     def enqueue(self, value):
#         if not self.tail:
#             new_tail = Node(value, None)
#             self.head = new_tail
#             self.tail = new_tail
#         else:
#             new_tail = Node(value, None)
#             old_tail = self.tail 
#             old_tail.next = new_tail
#             self.tail = new_tail
#         self.length += 1

#     def dequeue(self):
#         if not self.head:
#             return None
#         if self.head == self.tail: 
#             current_head = self.head
#             self.head = None
#             self.tail = None
#             self.length -= 1
#             return current_head.value
#         else:
#             current_head = self.head
#             self.head = current_head.next
#             self.length -= 1
#             return current_head.value
