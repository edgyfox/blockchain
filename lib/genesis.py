# -*- coding: utf-8 -*-

import BlockChainModule as BCM
import pandas as pd
    
def tamperTransaction():
    
    chain_index = int(input("Block index to tamper: "))
    print(blockchain.chain[chain_index].get_block_data)
    trans_index = int(input("Transaction to tamper: "))
    print(blockchain.chain[chain_index].data[trans_index])
    tampered_amount = float(input("Tampered amount: "))
    blockchain.chain[chain_index].data[trans_index].amount = tampered_amount

df_ledger = pd.read_csv("./ledger1/dump1.csv",delimiter = ',', header = 0, index_col = 0)
blockchain = BCM.Blockchain() 

for i in range(len(df_ledger)):
    trans = df_ledger.loc[i]
    blockchain.add_data(trans['sender'], trans['receiver'], trans['amount'])

while True:
    
    print("\n\n1. Add transaction")
    print("2. Display chain")
    print("3. Check validity")
    print("4. Current data")
    print("5. Tamper")
    print("0. Exit")
    ch = int(input("Enter option: "))
    
    if ch == 1:
        sender = input("Enter sender: ")
        receiver = input("Enter receiver: ")
        amount = float(input("Enter amount: "))
        blockchain.add_data(sender, receiver, amount)
        
    elif ch == 2:
        print(blockchain)
        
    elif ch == 3:
        print("IS CHAIN VALID: ", blockchain.isValid)
        
    elif ch == 4:
        print(blockchain.current_data)
        
    elif ch == 5:
        tamperTransaction()
    
    elif ch == 0:
        break