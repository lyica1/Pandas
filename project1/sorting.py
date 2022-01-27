import dataSets

# Sort rows descendingly by the index
print(dataSets.df.sort_index(axis=0, ascending=False))

# Sort col2 and col1 by values
print(dataSets.df.sort_values(by=['col1','col2'],ascending=False))
print(ord("G"))