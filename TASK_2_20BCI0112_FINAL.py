#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np

df=pd.read_csv('data/weatherAUS.csv')


# In[3]:


df.columns


# In[6]:


df


# # LEVEL 1
# 

# In[4]:


df['MaxTemp'].mean()


# In[5]:


df['MinTemp'].mean()


# In[8]:


f=df['Location']=='Cobar'
df[f]['MaxTemp'].mean()


# In[39]:


f=pd.isnull(df['Sunshine'])
g=pd.isnull(df['Evaporation'])
x=tuple()
y=tuple()
x=df[f]['Sunshine'].shape
print("NUMBER OF NULL VALUE IN Sunshine COLUMN= ",x[0])
y=df[g]['Evaporation'].shape
print("NUMBER OF NULL VALUE IN Evaporation COLUMN= ",y[0])


# # LEVEL 2

# In[48]:


df=pd.read_csv('data/weatherAUS.csv')


# In[51]:


df['Evaporation'].replace({np.nan:df['Evaporation'].mean()},inplace=True)


# In[52]:


df


# In[64]:


df.drop(columns=pd.isnull(df).columns)
#inplace=True for making changes permanent


# In[62]:


df.drop(columns=['Date'])
#inplace=True for making changes permanent


# # LEVEL 3

# In[11]:


def show_data(location):
    filt=df['Location']==location
    return df.loc[filt]


# In[17]:


pd.set_option('display.max_columns',20)
pd.set_option('display.max_rows',20)


# In[18]:


x=show_data('Uluru')
x


# In[ ]:




