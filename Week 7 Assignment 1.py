#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd


# In[5]:


df = pd.read_csv('C://Users/Nanda/Downloads/all_040_in_01.csv')


# In[6]:


df.head()


# In[7]:


df.shape


# In[8]:


#Page 9 
import pandas as pd
df = pd.read_excel('C://Users/Nanda/Downloads/BNK02.xls')
df.head()


# In[9]:


df.to_excel("output.xlsx")


# In[ ]:




