import csv
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate

def line_printer(n):
    for i in range(n):
        print()



            
df = pd.read_csv('train.csv')
df.drop(columns=['Ticket','Name'])
del df['Ticket']
del df['Name']

for index, row in df.iterrows():
    currentage = row["Age"]
    agebrack = 0
    if currentage == None:
        agebrack = -1
    elif currentage <= 10:
        agebrack = 0
    elif currentage > 10 and currentage <= 18:
        agebrack = 1
    elif currentage > 18 and currentage <= 30:
        agebrack = 2
    elif currentage > 30 and currentage <= 65:
        agebrack = 3
    elif currentage > 65:
        agebrack = 4
    else:
        agebrack = 1000
    df.at[index,'Age'] = agebrack

agedf = df[['Age','Survived']].groupby(['Age'], as_index=False).mean().sort_values(by='Age', ascending=True)



print(tabulate(agedf, headers="keys"))

line_printer(3)

print(tabulate(df.describe(), headers="keys"))

