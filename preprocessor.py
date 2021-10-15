'''
@author: Sougata Saha
Institute: University at Buffalo
'''

import collections
from nltk.stem import PorterStemmer
import re
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')


class Preprocessor:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        self.ps = PorterStemmer()

    def get_doc_id(self, doc):
        """ Splits each line of the document, into doc_id & text.
            Already implemented"""
        arr = doc.split("\t")
        return int(arr[0]), arr[1]

    def tokenizer(self, text):
        tokenized_doc = text
        tokenized_doc = re.sub(r"[^a-zA-Z0-9]+", ' ', text)
        print("specialchar",tokenized_doc)
        re.sub(' +', ' ', tokenized_doc)
        print("extra space",tokenized_doc)
        
        return tokenized_doc
