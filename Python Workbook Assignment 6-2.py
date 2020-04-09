#!/usr/bin/env python
# coding: utf-8

# In[16]:


#Python Workbook Assignment 6-2
import pandas as pd
Location = "C:\MUNJA_DATA\Courses\Data Visualization\learn-data-analysis-w-python-master\datasets\gradedata.csv"
df = pd.read_csv(Location)
df.head()


# In[17]:


import statsmodels.formula.api as sm
result = sm.ols(
formula='grade ~ age + exercise + hours',
data=df).fit()
result.summary()


# In[19]:


df['numGender'] = [1 if x =='female' else 0 for x in df['gender']] 


# In[20]:


df


# In[21]:


import statsmodels.formula.api as sm
result = sm.ols(
formula='grade ~ age + exercise + hours + numGender',
data=df).fit()
result.summary()


# In[ ]:


#yes by adding gender to regression, the value of R-squared has been improved from 0.664 to 0.665

