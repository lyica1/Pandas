import os

import pandas as pd

#Try to invoke .head() before you get started. It will give you some general concepts of what data is included in the csv files
#You will face some data type issues. Make sure to convert data if needed,

#Problem1: Merge every csv files into a single csv file (merge the 12months of sales data into a single csv file)
#Tip: Try to iterate every files in salesData folder and read_csv each file and concatenate using pandas dataframe



print("Problem1 : ")
sales_datas = os.listdir('salesData')
print(sales_datas)
new_df = pd.DataFrame()
for i in range(0,len(sales_datas)):
    file='salesData/'+sales_datas[i]
    df=pd.read_csv(file)
    new_df = pd.concat([new_df,df])
new_df.to_csv('Sales_All_2019.csv')
print('==================================================')


#Problem2: There will be duplicate column names stored in the generated csv file as a value since each csv file has column names and we've just concatenated them. So drop those rows
#Tip: This one is tricky. Try to filter out rows that contain column names. Ex) data['Product'].str[0:7] != 'Product'. Read this article. https://cmdlinetips.com/2018/02/how-to-subset-pandas-dataframe-based-on-values-of-a-column/


print("Problem2 : ")
new_df = pd.read_csv('Sales_All_2019.csv')
new_df.drop(columns=['Unnamed: 0'],inplace=True)
columns=['Order ID','Product','Quantity Ordered','Price Each','Order Date','Purchase Address']
new_df=new_df[~new_df.isin(columns)]
print(new_df.head(10))
print('==================================================')


#Problem3: Drop NaN rows. Some rows contain NaN.


print("Problem3 : ")
new_df.dropna(inplace=True)
print(new_df.head(10))
print('==================================================')


#Problem4: Add a month column to the generated csv file from the above
#Tip: extract month from order date


print("Problem4 : ")
datelist=[]
for idx, row in new_df.iterrows():
    datelist.append(row['Order Date'].split('/')[0])
new_df['Month'] = datelist
print(new_df.head(10))
print('==================================================')


#Problem5: Add a sales column. A result of Quantity Ordered * Price Each will be stored


print("Problem5 : ")
new_df[['Quantity Ordered','Price Each']]=new_df[['Quantity Ordered','Price Each']].astype('float')
new_df['Sales']=new_df['Quantity Ordered']*new_df['Price Each']
print(new_df.head(10))
print('==================================================')


#Problem6: What was the best month for sales (Highest sales)


print("Problem6 : ")
print(new_df.groupby('Month')['Sales'].mean())
print("Max Value : "+ str(new_df.groupby('Month')['Sales'].mean().max()))