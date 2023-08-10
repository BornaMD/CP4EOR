#Exercise 0
with open("Customer.txt", "r") as fh:
  tbl = []
  for i in len(fh):
    tbl[i][0] = fh.readlines([i][0]).split(',')
    tbl[i][1] = fh.readlines([i][1]).split(',')
    tbl[i][2] = fh.readlines([i][2]).split(',')

#answer
tbl=[]
fh=open("Customers.txt")
lines=fh.readlines()
fh.close()
for L in lines:
  tbl.append(L.strip().split(','))
print(tbl)

s=0
for row in tbl:

#niet af

# Pandas


# Exercise 1
import numpy as np
import pandas as pd

df=pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv", )