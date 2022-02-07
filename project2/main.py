import os

import pandas as pd

#Try to invoke .head() before you get started. It will give you some general concepts of what data is included in the csv files
#You will face some data type issues. Make sure to convert data if needed,

#Problem1: Merge every csv files into a single csv file (merge the 12months of sales data into a single csv file)
#Tip: Try to iterate every files in salesData folder and read_csv each file and concatenate using pandas dataframe

#Problem2: There will be duplicate column names stored in the generated csv file as a value since each csv file has column names and we've just concatenated them. So drop those rows
#Tip: This one is tricky. Try to filter out rows that contain column names. Ex) data['Product'].str[0:7] != 'Product'. Read this article. https://cmdlinetips.com/2018/02/how-to-subset-pandas-dataframe-based-on-values-of-a-column/

#Problem2: Add a month column to the generated csv file from the above
#Tip: extract month from order date

#Problem3: Drop NaN rows. Some rows contain NaN.

#Problem4: Add a sales column. A result of Quantity Ordered * Price Each will be stored

#Problem5: What was the best month for sales (Highest sales)
