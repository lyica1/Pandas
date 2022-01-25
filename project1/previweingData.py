import dataSets

# Previewing data
# Displays the top 5 rows. Accepts an optional int parameter - num. of rows to show
print(dataSets.df.head())

# Similar to head, but displays the last rows
print(dataSets.df.tail())

# The dimensions of the dataframe as a (rows, cols) tuple
print(dataSets.df.shape)

# The number of columns. Equal to df.shape[0]
print(len(dataSets.df))

# An array of the column names
print(dataSets.df.columns)

# Columns and their types
print(dataSets.df.dtypes)

# Converts the frame to a two-dimensional table
print(dataSets.df.values)

# Displays descriptive stats for all columns
print(dataSets.df.describe())
