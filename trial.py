import csv
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate

def line_printer(n):
    for i in range(n):
        print()

def return_survival(survdata, pclass, sex):
    for i in survdata:
        if i[0] == pclass and i[1] == sex:
            return float(int(i[2]*10000))/100
            
df = pd.read_csv('train.csv')
df.drop(columns=['Ticket','Name'])
del df['Ticket']
del df['Name']


line_printer(3)

print(tabulate(df.describe(), headers="keys"))

sdf = df[['Sex', 'Survived']].groupby(['Sex'], as_index=False).mean().sort_values(by='Sex', ascending=True)
cdf = df[['Pclass', 'Survived']].groupby(['Pclass'], as_index=False).mean().sort_values(by='Pclass', ascending=True)
scdf = df[['Sex','Pclass', 'Survived']].groupby(['Pclass','Sex'], as_index=False).mean().sort_values(by='Pclass', ascending=True)


print("_"*40)
print("Survival by Sex AND Class: ")

line_printer(2)

print(tabulate(scdf, headers="keys"))


print("_"*40)
print("Survival by Sex")

line_printer(2)

print(tabulate(sdf, headers="keys"))

print("_"*40)
print("Survival by Class: ")

line_printer(2)

print(tabulate(cdf, headers="keys"))
# biglist =[]
# for index, rows in scdf.iterrows():
#     templist = []
#     templist.append(int(rows["Pclass"]))
#     templist.append(str(rows["Sex"]))
#     templist.append(float(rows["Survived"]))
#     biglist.append(templist)
#     templist = []


# with open('test.json') as json_file: 
#     data = json.load(json_file) 
    
# for i in data:
#     surv_chance = return_survival(biglist, i["Pclass"], i["Sex"])
#     print()
#     print("Passenger ID: "+str(i["PassengerId"]))
#     print ("Sex: ", i["Sex"])
#     print ("Class: ", i["Pclass"])
#     print ("Survival: "+ str(surv_chance)+"%")
#     print()


