#!/usr/bin/env python
# coding: utf-8

# In[1]:


pwd


# In[3]:


import pandas as pd
import numpy as np
df = pd.read_csv("employees.csv")

print(df.head())
print(df.dtypes)
print(df.describe())


# In[4]:


print('Salary')
print(df['Salary'].head(10))


# In[5]:


print(df['Gender'].head(10))


# In[6]:



missing_value_formats = ["n.a.","?","NA","n/a", "na", "--"]
df = pd.read_csv("employees.csv", na_values = missing_value_formats)

print(df['Gender'].head(10))


# In[8]:


import pandas as pd

missing_value_formats = ["n.a.","?","NA","n/a", "na", "--"]
df = pd.read_csv("employees.csv", na_values = missing_value_formats)

def make_int(i):
    try:
        return int(i)
    except:
        return pd.np.nan


df['Salary'] = df['Salary'].map(make_int)
print(df['Salary'].head())


# In[9]:


print(df['Gender'].isnull().head(10)) 
print(df['Gender'].notnull().head(10))


# In[10]:


null_filter = df['Gender'].notnull()
print(df[null_filter].head())


# In[11]:


print(df.isnull().values.any())


# In[12]:


print(df.isnull().sum())


# In[13]:


new_df = df.dropna(axis=0)

print(new_df.isnull().values.any())


# In[14]:


# drop all rows with atleast one NaN
new_df = df.dropna(axis = 0, how ='any')  

# drop all rows with all NaN
new_df = df.dropna(axis = 0, how ='all')

# drop all columns with atleast one NaN
new_df = df.dropna(axis = 1, how ='any')

# drop all columns with all NaN
new_df = df.dropna(axis = 1, how ='all')


# In[15]:


df['Salary'].fillna(0)


# In[16]:


df['Gender'].fillna('No Gender')


# In[17]:


df['Salary'].fillna(method='pad')


# In[18]:


df['Salary'].fillna(method='bfill')


# In[19]:


df['Salary'].fillna(df['Salary'].median())


# In[20]:


df['Salary'].fillna(int(df['Salary'].mean()))


# In[21]:


df['Salary'].replace(to_replace = np.nan, value = 0)


# In[22]:


df['Salary'].interpolate(method='linear', direction = 'forward')


# In[ ]:




