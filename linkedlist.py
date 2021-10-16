'''
@author: Sougata Saha
Institute: University at Buffalo
'''

import math
from collections import OrderedDict

class Node:

    def __init__(self, value=None, next=None, tf_idf=None, skip=None):
        """ Class to define the structure of each node in a linked list (postings list).
            Value: document id, Next: Pointer to the next node
            Add more parameters if needed.
            Hint: You may want to define skip pointers & appropriate score calculation here"""
        self.value = value
        self.tf_idf = tf_idf
        self.next = next
        self.skip = skip


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
            if self.skip_length<=1:
                return traversal
            else:
                h = self.start_node
                while h is not None:
                    traversal.append(h.value)
                    h=h.skip
            print(traversal)
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
                                        "tf_idf":n.tf_idf})
                traversal.append(str(node_val)+"\n"+"\t"*cnt)
                cnt += 1
                n = n.next
            return "->".join(traversal)
        
    def add_skip_connections(self):
        n_skips = math.floor(math.sqrt(self.length))
        if n_skips * n_skips == self.length:
            n_skips = n_skips - 1
        self.n_skips = n_skips
        self.skip_length = int(round(math.sqrt(self.length),0))
        """ Write logic to add skip pointers to the linked list. 
            This function does not return anything.
            To be implemented."""
        h_skip = self.start_node
        #print("skip ",h_skip.value)
        h_next = self.start_node
        #print("node ",h_next.value)
        if self.skip_length <= 1:
            return
        else:
            skips = self.n_skips
            while (skips>0):
                skips -= 1
                skip_len = self.skip_length
                while(skip_len>0):
                    skip_len -= 1
                    h_next = h_next.next
                    #print("node ",h_next.value)
                h_skip.skip = h_next
                h_skip = h_skip.skip
                #print("skip ",h_skip.value) 

    def insert_at_end(self, tf, value):
        new_node = Node(value=value, tf_idf=tf)
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

