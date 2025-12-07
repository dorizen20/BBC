import pandas as pd

file = pd.read_csv("tested.csv")

print(file.isnull().sum())

print(file.dtypes)
'''
n = int(input("кол-во строк: "))
print(file.head(n))
'''
print(file['Age'].describe())

columns = file.shape[1]
lines = file.shape[0]
print(columns, lines)

print(file.isnull().sum().sum())

file['Age'] = file['Age'].fillna(file['Age'].median())

empty_lines = file[file.isnull().any(axis=1)].index

if len(empty_lines) >= 20:
    file = file.drop(empty_lines[:20])
else:
    file = file.dropna()
