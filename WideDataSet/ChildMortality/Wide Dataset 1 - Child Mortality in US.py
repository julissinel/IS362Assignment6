#!/usr/bin/env python
# coding: utf-8

# In[26]:


import pandas as pd


# # Under Five Mortality Rate in USA
# 

# In[57]:


data = pd.read_csv(r"C:\Users\naila.latif\Desktop\USAChildMortality.csv")


# In[58]:


data.head()


# In[52]:


l = pd.wide_to_long(data,stubnames=['Under.five.Deaths','IMR','NMR','U5MR'], i=['ISO Code',
 'CountryName',
 'Uncertainty bounds*'],j='Year',sep='.',suffix='\w+')


# In[53]:


l


# In[105]:


l.head()


# Checking Under five Mortality Trends
# 

# In[103]:


import matplotlib.pyplot as plt
l.iloc[0:66].plot(y="Under.five.Deaths",figsize=(6,6))
plt.xticks(rotation=90)


# In[ ]:




