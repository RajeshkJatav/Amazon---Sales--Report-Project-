#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[6]:


df = pd.read_csv(r'C:\Users\RAJESH KUMAR\Desktop\Python projects\Python_Amazon_Sales_Analysis-main\Python_Amazon_Sales_Analysis-main\Amazon Sale Report.csv', encoding='unicode_escape')


# In[8]:


df.shape


# In[9]:


df.head()


# In[11]:


df.tail() # Details about last 5 data


# In[14]:


df.info()


# In[13]:


df.drop(['New', 'PendingS'], axis =1 , inplace = True)


# In[17]:


pd.isnull(df).sum()


# In[19]:


#drop null values
df.dropna( inplace = True)


# In[20]:


df.shape


# In[21]:


df.columns


# In[24]:


df['ship-postal-code'] = df['ship-postal-code'].astype('int')


# In[26]:


df['ship-postal-code'].dtypes


# In[30]:


df['Date'] =pd.to_datetime(df['Date'])


# In[28]:


df.columns


# In[33]:


#reanmes columns
df.rename(columns={'Qty':'Quantity'})


# In[35]:


df.describe()


# In[39]:


df.describe(include='object')


# In[43]:


df[['Qty','Amount']].describe()


# In[44]:


df.columns


# In[45]:


ax=sns.countplot(x='Size', data=df


# In[97]:


import seaborn as sns
import matplotlib.pyplot as plt

# Set the figure size
plt.figure(figsize=(20, 8))

# Create the countplot
ax = sns.countplot(x='Size', data=df)

# Add labels to the bars
for bar in ax.containers:
    ax.bar_label(bar)

plt.show()


# In[ ]:


Note = from the above graph we can see that most of the people buys M-size 


# In[ ]:


GROUP BY


# In[64]:


df.groupby(['Size'], as_index=False)['Qty'].sum().sort_values(by='Qty', ascending=False)


# In[75]:


import seaborn as sns
import matplotlib.pyplot as plt

# Grouping, summing, and sorting
grouped_df = df.groupby(['Size'], as_index=False)['Qty'].sum().sort_values(by='Qty', ascending=False)

# Creating a barplot
plt.figure(figsize=(20, 8))  # corrected parameter name
sns.barplot(x='Size', y='Qty', data=grouped_df)

plt.show()


# In[ ]:





# In[77]:


plt.figure(figsize=(20,8))
ax= sns.countplot(data=df, x='Courier Status', hue= 'Status')


# In[ ]:


Note: From above Graph the majority of the orders are shipped through the courier.


# In[91]:


# Set the figure size
plt.figure(figsize=(20, 8))

# Plot the histogram
df['Size'].hist()

plt.show()


# In[90]:


df['Category'] = df['Category'].astype(str)
column_data = df['Category']
plt.figure(figsize=(20, ))
plt.hist(column_data, bins=30, edgecolor='Black')
plt.xticks(rotation=90)
plt.show()


# In[ ]:


Note: From above Graph you can see that most of the buyers are T-shirt


# In[81]:


# Checking B2B Data  by using pie chart 
B2B_Check = df['B2B'].value_counts()

#  Plot the pie chart
plt.pie(B2B_Check, labels=B2B_Check, autopct='%1.1f%%')
#plt.axis('equal')
plt.show()


# In[82]:


# Checking B2B Data  by using pie chart 
B2B_Check = df['B2B'].value_counts()

#  Plot the pie chart
plt.pie(B2B_Check, labels=B2B_Check.index, autopct='%1.1f%%')
#plt.axis('equal')
plt.show()


# In[ ]:


Note : From above chart we can see that maximum i.e. 99.3% of buyers are retailers and 0.7% are B2B buyers


# In[89]:


# Prepare data for scatter plot
x_data = df['Category']  
y_data = df['Size'] 

# Set the figure size
plt.figure(figsize=(20, 8))

# Plot the scatter plot
plt.scatter(x_data, y_data)
plt.xlabel('Category')  
plt.ylabel('Size')  
plt.title('Scatter Plot') 
plt.show()


# In[99]:


# Plot count of cities by state

plt.figure(figsize=(20, 8))
sns.countplot(data=df, x='ship-state')
plt.xlabel('ship-state')
plt.ylabel('count')
plt.title('Distribution of State')
plt.xticks(rotation=90)
plt.show()


# In[98]:


# top_10_States 
top_10_state = df['ship-state'].value_counts().head(10)
# Plot count of cities by state
plt.figure(figsize=(20, 8))
sns.countplot(data=df[df['ship-state'].isin(top_10_state.index)], x='ship-state')
plt.xlabel('ship-state')
plt.ylabel('count')
plt.title('Distribution of  State')
plt.xticks(rotation=45)
plt.show()


# In[ ]:


Note: From above Graph you can see that most of the buyers are Maharashtra state
Conclusion
The data analysis reveals that the business has a significant customer base in Maharashtra state, mainly serves retailers,
fulfills orders through Amazon, experiences high demand for T-shirts, and sees M-Size as the preferred choice among buyers.
 

