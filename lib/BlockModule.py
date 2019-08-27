# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 17:49:09 2019

@author: an095t
"""
import time
import hashlib

class Block(object):

    #initialise block with index, nonce, previous hash, data
    def __init__(self, index, nonce, hash_previous, data):

        self.index = index
        self.nonce = nonce
        self.hash_previous = hash_previous
        self.data = data
        self.timestamp = time.time()
        self.flag_hash = "0"

    #reutrn hash of the block
    @property
    def compute_hash(self):

        string_block = "{}{}{}{}{}".format(self.index, self.nonce, 
                        self.hash_previous, self.data, self.timestamp)
        self.flag_hash = hashlib.sha256(string_block.encode()).hexdigest()
        return self.flag_hash
    
    #get block's data
    @property
    def get_block_data(self):
        
        data = { "index": self.index,
                "hash": self.compute_hash,
                "prev_hash": self.hash_previous,
                "nonce": self.nonce,
                "data": self.data}        
        return data
    
    #set new nonce to check new hash
    def set_nonce(self, new_nonce):
        
        self.nonce = new_nonce
        
    def __repr__(self):
        
        block = {
                'index': self.index,
                'nonce': self.nonce,
                'prev_hash': self.hash_previous,
                'curr_hash': self.flag_hash,
                'data': self.data
                }
        return str(block)