import seaborn as sns
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

dataset = pd.read_csv("KVIS student dataset.csv")
dataset.columns = ['thai', 'region', 'english', 'income', 'expense', 'students']

def show_plot(dataset, region = 'all', show_none = False):
    __dataset = dataset
    if show_none == False:
        dataset = dataset[dataset['students'] != 0]
        print(dataset.iloc[:, 1:])

    plt.figure()
    if region == 'all':
        dataset = dataset
    elif region == 'northern':
        dataset = dataset[dataset.region == "Northern"]
    elif region == 'central':
        dataset = dataset[dataset.region == "Central"]
    elif region == 'northeastern':
        dataset = dataset[dataset.region == "Northeastern"]
    elif region == 'southern':
        dataset = dataset[dataset.region == "Southern"]
    else:
        dataset = dataset
    
    ax = sns.scatterplot(data = dataset, 
                        x = 'income', 
                        y = 'expense', 
                        hue = 'region', 
                        size = 'students',
                        sizes = (0, 100*__dataset.students.max()),
                        legend = False,
                        alpha = 0.7)

    for line in dataset.index:
        ax.text(dataset.income[line], dataset.expense[line], 
        dataset.english[line], horizontalalignment = 'center',
        verticalalignment = 'bottom',
        size = 4, color = 'black', weight = 'regular')
    
    plt.xlabel("Average Monthly Income Per Household (2015)")
    plt.ylabel("Average Monthly Expenditure Per Household (2015)")
    plt.title("Correlation of Income-Expense per Household and Number of Qualified Students to KVIS")
    plt.show()

show_plot(dataset, region = "all")


