import dataSets

# Do you know 2-D array?

# Selects only the column named 'col1'
print(dataSets.df['col1']) # 하나만 있을때 가능
# Select two columns
print(dataSets.df[['col1','col2']]) #여러개 추출시 브라켓 두개!
# Selects second row
print(dataSets.df.iloc[1])
# Selects rows 0-to-2 (index slicing is required)
print(dataSets.df.iloc[:3])
# First row, first column
print(dataSets.df.iloc[0,0])
# First 4 rows and first 2 columns
print(dataSets.df.iloc[2:4,1:2]) # 중요.