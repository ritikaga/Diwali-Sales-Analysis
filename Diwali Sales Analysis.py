# Diwali Sales Analysis
# Import Libaries
import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd
import numpy as np


# Loading .csv file using pandas
df = pd.read_csv(r"C:\Users\ritik\OneDrive\Documents\project data analysis\Python project\Diwali Sales Data.csv", encoding='unicode_escape')
print(df)

# Data Cleaning
# check the datatype of Each Column
df.info()

# find the rows and columns
print(df.shape)

# the top 5 rows of sales data
print(df.head())

# columns Names
print(df.columns)

# checl the datatype
print(df.dtypes)

# Remove Duplicates
print(df.duplicated())
df.drop_duplicates(inplace= True)
print(df)

# check Null Values
print(df.isnull().sum())

#delete umcessary columns and null data.
df.drop(["Status","unnamed1"],axis=1, inplace=True)
print(df.isnull().sum())
df.dropna(inplace= True)
print(df.isnull().sum())

# describe return description of the data in the DataFrame
print(df.describe())

# use describe() for specific columns
df[['Age', 'Orders', 'Amount']].describe()

# change the data type of amount
df['Amount']=df['Amount'].astype(int)


#Exploratory Data Analysis (EDA)

# Gender
# Plotting a bar chart for Gender and it's count

ax = sns.countplot(x = 'Gender',data = df)

for bars in ax.containers:
    ax.bar_label(bars)
plt.show()    

# plotting a bar chart for gender vs total amount

sales_gen = df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.barplot(x = 'Gender',y= 'Amount' ,data = sales_gen)
plt.show()   
'''we can see that most of the buyers are females and even the purchasing power of females are greater than men'''

#Age
ax = sns.countplot(data = df, x = 'Age Group', hue = 'Gender')

for bars in ax.containers:
    ax.bar_label(bars)
plt.show()   

# Total Amount vs Age Group
sales_age = df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x = 'Age Group',y= 'Amount' ,data = sales_age)    
plt.show()   
# we can see that most of the buyers are of age group between 26-35 yrs female

# State
# total number of orders from top 10 states

sales_state = df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data = sales_state, x = 'State',y= 'Orders')
plt.show()  

# total amount/sales from top 10 states

sales_state = df.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data = sales_state, x = 'State',y= 'Amount')
plt.show()  

#we can see that most of the orders & total sales/amount are from Uttar Pradesh, Maharashtra and Karnataka respectively

#Marital Status
ax = sns.countplot(data = df, x = 'Marital_Status')

sns.set(rc={'figure.figsize':(7,5)})
for bars in ax.containers:
    ax.bar_label(bars)
plt.show()  

sales_state = df.groupby(['Marital_Status', 'Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(6,5)})
sns.barplot(data = sales_state, x = 'Marital_Status',y= 'Amount', hue='Gender')
plt.show()  
#we can see that most of the buyers are married (women) and they have high purchasing power

#Occupation
sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data = df, x = 'Occupation')

for bars in ax.containers:
    ax.bar_label(bars)
plt.show()  


sales_state = df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Occupation',y= 'Amount')    
plt.show()  
#we can see that most of the buyers are working in IT, Healthcare and Aviation sector

#Product Category
sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data = df, x = 'Product_Category')

for bars in ax.containers:
    ax.bar_label(bars)
plt.show()  


sales_state = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_Category',y= 'Amount')
plt.show()  
# we can see that most of the sold products are from Food, Clothing and Electronics category
sales_state = df.groupby(['Product_ID'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_ID',y= 'Orders')
plt.show()  


# top 10 most sold products (same thing as above)

fig1, ax1 = plt.subplots(figsize=(12,7))
df.groupby('Product_ID')['Orders'].sum().nlargest(10).sort_values(ascending=False).plot(kind='bar')
plt.show()  


#CONCLUSION
#Married women age group 26-35 yrs from UP, Maharastra and Karnataka working in IT, Healthcare and Aviation are more likely to buy products from Food, Clothing and Electronics category

#Thank you!