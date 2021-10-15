'''
@author: Sougata Saha
Institute: University at Buffalo
'''

from linkedlist import LinkedList
from collections import OrderedDict


class Indexer:
    def __init__(self):
        """ Add more attributes if needed"""
        self.inverted_index = OrderedDict({})

    def get_index(self):
        """ Function to get the index.
            Already implemented."""
        return self.inverted_index

    def generate_inverted_index(self, doc_id, tokenized_document):
        tf_values = {}
        
        for t in tokenized_document:
            if t not in tf_values:
                tf_values[t] = 1
            else:
                tf_values[t] += 1
        
        for t in tf_values:
            self.add_to_index(t, doc_id, tf_values[t])

    def add_to_index(self, term_, doc_id_,tf_):
        
        if term_ not in self.inverted_index:
            self.inverted_index[term_] = LinkedList()
            self.inverted_index[term_].insert_at_end(tf_,doc_id_)
        else:
            cur_docids = self.inverted_index[term_].traverse_list()
            if doc_id_ not in cur_docids:
                self.inverted_index[term_].insert_at_end(tf_,doc_id_)
        return

    def sort_terms(self):
        """ Sorting the index by terms.
            Already implemented."""
        sorted_index = OrderedDict({})
        for k in sorted(self.inverted_index.keys()):
            sorted_index[k] = self.inverted_index[k]
        self.inverted_index = sorted_index

    def add_skip_connections(self):
        """ For each postings list in the index, add skip pointers.
            To be implemented."""
        raise NotImplementedError

    def calculate_tf_idf(self):
        """ Calculate tf-idf score for each document in the postings lists of the index.
            To be implemented."""
        total_docs_len = len(self.inverted_index.keys())
        for term in self.inverted_index:
            postings_list_len = self.inverted_index[term].length
            idf_ = total_docs_len / postings_list_len
            self.inverted_index[term].idf= idf_
            print(term, idf_)
            plist = self.inverted_index[term]
            if plist is not None:
                h = plist.start_node
                while h:
                    cur_tf = h.tf_idf
                    print("old",h.value,h.tf_idf)
                    h.tf_idf = idf_ * cur_tf
                    print("new",h.value,h.tf_idf)
                    h=h.next

        return
