import matplotlib.pyplot as plt
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules 

data = pd.read_csv("liqwinners.csv")

transactions = []
for year, characters in data.groupby('year'):
    transactions.append(list(characters['character']))

print(transactions)


# preprocessing
te = TransactionEncoder()
te_arr = te.fit(transactions).transform(transactions)

df = pd.DataFrame(te_arr, columns=te.columns_)

# Apriori
frequent_itemsets = apriori(df, min_support=0.025, use_colnames=True)
print(frequent_itemsets)
frequent_itemsets.to_csv("frequent_itemsets.csv")

rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.7)



rules.to_csv("meleeTournamentRules.csv")

print(rules) 