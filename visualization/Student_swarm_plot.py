# -*- coding: utf-8 -*-
"""
Created on Tue May 28 12:11:15 2019

@author: azuromalachite
"""

# Create bee swarm plot: Number of students in 2nd round admission 


import matplotlib.pyplot as plt
import pandas as pd 
import seaborn as sns

# Load the dataframe
df = pd.read_csv("KVIS student dataset.csv")

# Check the column name
for col in df.columns: 
    print(col) 

plt.figure(figsize=(8, 10))
sns.swarmplot(x='Region',y='Number of students in 2nd KVIS admission round (2019)',data = df)
sns.set(font_scale=1)
plt.xlabel('Region')
plt.ylabel('Number of students in 2nd KVIS admission round (2019)')
plt.show()
plt.close()

