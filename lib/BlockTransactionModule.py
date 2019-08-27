# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 17:29:26 2019

@author: an095t
"""

class BlockTransaction:
    
    def __init__(self, sender, receiver, amount):
        
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        
    def __repr__(self):
        
        transaction = {
                "sender": self.sender,
                "receiver": self.receiver,
                "amount": self.amount}
        return str(transaction)
    