'''
@author: Sougata Saha
Institute: University at Buffalo
'''

import math
from collections import OrderedDict

class Node:

    def __init__(self, value=None, next=None, tf=None):
        """ Class to define the structure of each node in a linked list (postings list).
            Value: document id, Next: Pointer to the next node
            Add more parameters if needed.
            Hint: You may want to define skip pointers & appropriate score calculation here"""
        self.value = value
        self.tf = tf
        self.next = next


class LinkedList:
    """ Class to define a linked list (postings list). Each element in the linked list is of the type 'Node'
        Each term in the inverted index has an associated linked list object.
        Feel free to add additional functions to this class."""
    def __init__(self):
        self.start_node = None
        self.end_node = None
        self.length, self.n_skips, self.idf = 0, 0, 0.0
        self.skip_length = None

    def traverse_list(self):
        traversal = []
        if self.start_node is None:
            print("List has no element")
            return
        else:
            n = self.start_node
            while n is not None:
                traversal.append(n.value)
                n=n.next
            return traversal

    def traverse_skips(self):
        traversal = []
        if self.start_node is None:
            return
        else:
            """ Write logic to traverse the linked list using skip pointers.
                To be implemented."""
            raise NotImplementedError
            return traversal
        
    def traverse_list_extra(self):
        traversal = []
        if self.start_node is None:
            print("List has no element")
            return
        else:
            n = self.start_node
            # Start traversal from head, and go on till you reach None
            cnt = 1
            while n is not None:
                node_val = OrderedDict({"id":n.value, 
                                        "tf":n.tf})
                traversal.append(str(node_val)+"\n"+"\t"*cnt)
                cnt += 1
                n = n.next
            return "->".join(traversal)
        
    def add_skip_connections(self):
        n_skips = math.floor(math.sqrt(self.length))
        if n_skips * n_skips == self.length:
            n_skips = n_skips - 1
        """ Write logic to add skip pointers to the linked list. 
            This function does not return anything.
            To be implemented."""
        raise NotImplementedError

    def insert_at_end(self, tf, value):
        new_node = Node(value=value, tf=tf)
        self.length += 1
        n = self.start_node

        if self.start_node is None:
            self.start_node = new_node
            self.end_node = new_node
            return

        elif self.start_node.value >= value:
            self.start_node = new_node
            self.start_node.next = n
            return

        elif self.end_node.value <= value:
            self.end_node.next = new_node
            self.end_node = new_node
            return

        else:
            while n.value < value < self.end_node.value and n.next is not None:
                n = n.next

            m = self.start_node
            while m.next != n and m.next is not None:
                m = m.next
            m.next = new_node
            new_node.next = n
        return

