import pandas as pd
import numpy as np

file = pd.read_csv("/tested.csv", index_col = 0)
print(file.isnull.sum())