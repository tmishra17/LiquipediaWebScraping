import numpy as np 
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules 

data = pd.read_csv("liqwinners.csv")

transactions = []
for year, characters in data.groupby('year'):
    transactions.append(list(characters['character']))

print(len(data['year']))

# preprocessing
te = TransactionEncoder()
te_arr = te.fit(transactions).transform(transactions)
df = pd.DataFrame(te_arr, columns=te.columns_)
# Apriori
freqeunt_itemsets = apriori(df, min_support=0.025, use_colnames=True)
rules = association_rules(freqeunt_itemsets, metric="confidence", min_threshold=0.7)



rules.to_csv("meleeTournamentRules.csv")

print(rules) 