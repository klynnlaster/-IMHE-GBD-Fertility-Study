#!/usr/bin/env python
# coding: utf-8

# In[13]:


import numpy as np


# In[14]:


import pandas as pd


# In[15]:


df = pd.read_csv('IHME_FERTILITY_1950_2019.CSV', index_col = "location_id")


# In[16]:


df.head()


# In[17]:


df.drop(columns = df.loc[:,'location_name':'age_group_name'], inplace = True)


# In[19]:


df.drop(columns = df.loc[:,'measure_id':'metric_name'], inplace = True)


# In[20]:


df.drop(columns = df.loc[:,'upper':'lower'], inplace = True)


# In[42]:


globalDf = df.loc[1]


# In[43]:


usDf = df.loc[102]


# In[44]:


globalDf = globalDf.rename(columns = {'year_id':'Year', 'val':'Global'})


# In[45]:


globalDf = globalDf.set_index('Year')


# In[48]:


usDf = usDf.rename(columns = {'year_id':'Year', 'val':'US'})


# In[49]:


usDf = usDf.set_index('Year')


# In[55]:


result = globalDf.join(usDf)


# In[56]:


result


# In[57]:


import matplotlib.pyplot as plt


# In[75]:


plt.plot(result['Global'], 'r-.', label = 'Global' )
plt.plot(result['US'], 'b-.', label = 'US')
plt.title('Fertility Rates 1950 - 2019: Global vs US')
plt.xlabel('Date')
plt.ylabel('Rate')
plt.legend(loc="upper right")


# In[ ]:




