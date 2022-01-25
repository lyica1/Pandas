import numpy as np
import pandas as pandas

# Datasets
df = pandas.DataFrame({
   'col1': ['Item0', 'Item0', 'Item1', 'Item1'],
   'col2': ['Gold', 'Bronze', 'Gold', 'Silver'],
   'col3': [1, 2, np.nan, 4]
})
