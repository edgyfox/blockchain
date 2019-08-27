# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 17:53:11 2019

@author: an095t
"""
import BlockModule as BM
import BlockTransactionModule as BTM

class Blockchain(object):
    
    #initialise chain with array of blocks, difficulty, genesis block
    def __init__(self):
        
        self.chain = []        
        self.current_data = []        
        self.initialise_blockchain()        
        self.difficulty = 2
        self.block_size = 3
        
    #build genesis block with index, nonce and previous hash as 0
    def initialise_blockchain(self):
        
        genesis_data = BTM.BlockTransaction(None, None, 0)
        genesis = self.build_new_block(index = 0, nonce = 0, hash_previous = "0", data = [genesis_data])
        genesis.compute_hash
        self.chain.append(genesis)
        
    #get hash of the current block
    @property
    def get_last_hash(self):
        
        return self.chain[-1].compute_hash
       
    #build new block with index, nonce, previous hash, data
    def build_new_block(self, index, nonce, hash_previous, data):
        
        new_block = BM.Block(index, nonce, hash_previous, data)        
        return new_block
        
    #check validity of entire chain
    @property
    def isValid(self):
        
        for i in range(len(self.chain)):
            
            print("BLOCK:", i)
            current_flag_hash = self.chain[i].flag_hash
            current_calc_hash = self.chain[i].compute_hash
            print("CURRENT_FLAG_HASH: " + current_flag_hash)
            print("CURRENT_CALC_HASH: " + current_calc_hash)
            if current_flag_hash != current_calc_hash:
                return False
            
            if i > 0:
                previous_curr_hash = self.chain[i-1].compute_hash
                current_prev_hash = self.chain[i].hash_previous
                print("PREVIOUS_CURR_HASH: " + previous_curr_hash)
                print("CURRENT_PREV_HASH: " + current_prev_hash)
                if previous_curr_hash != current_prev_hash:
                    return False
        return True
    
    #solve for given difficulty, find nonce and append the new block
    def mine(self):
        
        diff = self.difficulty        
        nonce = 0        
        limit = 10000      
        
        nb_index = len(self.chain)
        nb_data = self.current_data
        nb_last_hash = self.get_last_hash
        new_block = self.build_new_block(nb_index,nonce,nb_last_hash,nb_data)
        
        while nonce <= limit:            
            new_block_hash = new_block.compute_hash
            if new_block_hash[:diff] == "0"*diff :
                self.chain.append(new_block)
                self.current_data = []
                print("NEW BLOCK GENERATED: " + new_block_hash)
                break
            nonce += 1
            new_block.set_nonce(nonce)
        print(self)
    
    #add data to current block
    def add_data(self, sender, receiver, amount):
        transaction = BTM.BlockTransaction(sender, receiver, amount)
        self.current_data.append(transaction)
        if len(self.current_data) == self.block_size:
            print("BLOCK LIMIT REACHED. MINING...")
            self.mine()
       
    #display entire chain
    def __repr__(self):
        
        chainMessage = "\n=============================================\n"
        for block in self.chain:
            chainMessage += "\t|\n\t|\n\t|\n" + str(block) + "\n"
            chainMessage += "=============================================\n"
        return chainMessage