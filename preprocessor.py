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
        tokenized_doc = text.lower()
        print("actual text",tokenized_doc)
        
        tokenized_doc = re.sub(r"[^a-zA-Z0-9]+", ' ', tokenized_doc)
        print("specialchar",tokenized_doc)
        
        re.sub(' +', ' ', tokenized_doc)
        print("extra space",tokenized_doc)
        
        tokens = tokenized_doc.split()
        
        stop_words = set(stopwords.words('english'))
        tokens_filtered = [w for w in tokens if not w.lower() in stop_words]
        
        stemmer = PorterStemmer()
        tokens_stemmed = [stemmer.stem(w) for w in tokens_filtered]
        
        final_tokens = tokens_stemmed
        
        print("final token",final_tokens)
        return final_tokens
