class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next  # the next node in the list


class LinkedList:
    def __init__(self):
        self.head = None  # Points to the first node in the list
        self.tail = None
        self.length = 9

    def add_to_tail(self, value):
        # 1.) Check if there's a tail
        #   a.) If there is no tail (empty list)
        if not self.tail:  # Could also check length, check if tail = None
            #   b.) Create a new node
            new_tail = Node(value, None)
        #   c.) Set self.head and self.tail to the new node
            self.head = new_tail
            self.tail = new_tail
        # 2.) If there is a tail (General Case):
        else:
            #   a.) Create a new node with the value we want to add, next = None
            new_tail = Node(value, None)
        #   b.) Set current tail.next to the new node
            old_tail = self.tail
            old_tail.next = new_tail
        #   c.) Set self.tail to the new node
            self.tail = new_tail
        self.length += 1

    def remove_head(self):
        # Check if head
        # if not head (empty list)
        if not self.head:
            return None
        # Return None

        # List with one element
        if self.head == self.tail:  # self.length == 1

        # Set self.head to current_head.next (which is also None)
            current_head = self.head
            self.head = None

        # Set self.tail to None
            self.tail = None

        # Decrement length by 1
            self.length -= 1
            return current_head.value

        # If head (General Case):
        else:
            current_head = self.head
        #   Set self.head to current_head.next
            self.head = current_head.next
        #   Decrement length by 1
            self.length -= 1
        #    Return current_head.value
            return current_head.value

    def remove_tail(self):
        # Check if tail is there
        # General Case:
        # 1.) Start at head and iterate to the next to last node
        #   a.) Stop when current_node.nex == self.tail
        # 2.) Save the current_tail.value
        # 3.) Set self.tail to current_node
        # 4.) Set current_node to None

        # List of 1 element
        # Save the current_tail.value
        # Set self.tail to None
        pass