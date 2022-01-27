import numpy as np
import pandas as pd

# Datasets
df = pd.DataFrame({
   'col1': ['Item0', 'Item0', 'Item1', 'Item1'],
   'col2': ['Gold', 'Bronze', 'Gold', 'Silver'],
   'col3': [1, 2, np.nan, 4]
})

data = pandas.read_csv("project1.csv", index_col="name")

