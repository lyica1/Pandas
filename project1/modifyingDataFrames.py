import dataSets

# Retrieve every data of Hyun, key method to consider, .loc
print(dataSets.data.columns) # Name 이 왜 출력이 안될까요? age 랑 address 만 출력됩니다.
print(dataSets.data.loc["Hyun"])
print("============================")
# Retrieve every ages, 'age'
print(dataSets.data['age'])
print("============================")
# Retrieve 2nd row(index = 1) by using iloc method
print(dataSets.data.iloc[1])
print("============================")
# Try .isnull() and see the result
print(dataSets.data.isnull())
print("============================")
# Fill missing(null,NaN) values with 0
data_1 = dataSets.data.fillna(0)
print(data_1)
print("============================")
# Drop rows that contain at least one Nan, null value
data_2=dataSets.data.dropna(axis=0)
print(data_2)
print("============================")
# **Iterate rows and modify a value in 'age' to 30, tip: .iterrows()
data_3 = dataSets.data
print(data_3)
print("----------------------------")
for index,row in data_3.iterrows():
    row['age']=30
    print(index+" changed")
print(data_3)
print("============================")
# Iterate columns and print column names, (age, address)
for col,item in dataSets.data.iteritems():
    print("column name :",col)
    print(item)
print("============================")



