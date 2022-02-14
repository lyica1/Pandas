import os

import pandas as pd
import matplotlib.pyplot as plt

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
print(new_df.groupby('Month')['Sales'].sum())
print("Max Value : "+ str(new_df.groupby('Month')['Sales'].sum().max()))
print('==================================================')

#Problem7: Plot the results
# Below is the answer. Make yourself to feel comfortable with this.
# results = new_df.groupby('Month').sum()
# months = range(1, 13)
# plt.bar(months, results['Sales'])
# plt.xticks(months)
# plt.ylabel('Sales in USD')
# plt.xlabel('Month')
# plt.show()
results = new_df.groupby('Month').sum()
months = range(1, 13)

plt.bar(months, results['Sales'])
plt.xticks(months)
plt.ylabel('Sales in USD')
plt.xlabel('Month')
plt.show()
print('==================================================')



#Problem8: What city had the highest number of sales?
#Tip: add a new column called 'City' You can retrieve city from Purchase Address column. Similar to problem 4.

citylist=[]
for idx, row in new_df.iterrows():
    citylist.append(row['Purchase Address'].split(',')[1])
new_df['City']=citylist
print(new_df.head())
print('==================================================')



#Problem9: Plot the results. Similar to Problem 7, but in this case, x-axis will be City instead of Month

results = new_df.groupby('City').sum()
cities=new_df['City'].unique()

plt.figure(figsize=(10,5))
plt.bar(cities, results['Sales'])
plt.xticks(cities, rotation=45)
plt.ylabel('Sales in USD')
plt.xlabel('City')
plt.show()
print('==================================================')

#Problem10: What time the products were sold the most?, create a bar graph here as well
#Tip: consider using .to_datetime() and create some additional columns, such as Hour..etc

new_df['Order Date']= pd.to_datetime(new_df['Order Date'])
new_df.info()
new_df['Order Date_time']=new_df['Order Date'].dt.hour
results = new_df.groupby('Order Date_time').sum()
x_labels=new_df['Order Date_time'].unique()

plt.figure(figsize=(10,5))
plt.bar(x_labels,results['Sales'])
plt.xticks(x_labels)
plt.xlabel('Time(hour)')
plt.ylabel('Sales in USD')
plt.show()
print('==================================================')

#Problem11: What product was sold the most?

results = new_df.groupby('Product').sum()
x_labels = new_df['Product'].unique()


plt.figure(figsize=(20,5))
plt.bar(x_labels,results['Quantity Ordered'])
plt.xticks(x_labels,rotation=45)
plt.xlabel('Products')
plt.ylabel('Number of Sold')
plt.show()