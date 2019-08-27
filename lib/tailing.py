# -*- coding: utf-8 -*-

import pandas as pd

df_ledger = pd.read_csv("./ledger1/dump1.csv",delimiter = ',', header = 0, index_col = 0)

transaction = ["Argha","Hemanth",100]

df_ledger.loc[len(df_ledger)] = transaction

df_ledger.to_csv("./ledger1/dump1.csv")