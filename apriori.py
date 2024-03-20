import numpy as np 
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules 

data = pd.read_csv("liqwinners.csv")

print(f"Data Head: {data.head()}")

print(f"Data Columns: {data.columns}")

# split data by year

print(f"Year: {data['tournament_year']}")

# basket_2004 = 
# basket_2005 = 
# basket_2006 = 
# basket_2007 = 
# basket_2008 = 
# basket_2009 = 
# basket_2010 = 
# basket_2011 = 
# basket_2012 = 
# basket_2014 = 
# basket_2015 = 
# basket_2016 = 
# basket_2017 = 
# basket_2018 = 
# basket_2019 = 
# basket_2020 = 
# basket_2021 = 
# basket_2022 = 
# basket_2023 = 

