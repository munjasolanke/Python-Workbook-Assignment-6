#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Python Workbook Assignment 6-1 
import pandas as pd
Location = "C:\MUNJA_DATA\Courses\Data Visualization\learn-data-analysis-w-python-master\datasets\gradedata.csv"
df = pd.read_csv(Location)
df.head()


# In[2]:


df = df.sort_values(by=['fname','age','grade'],
ascending=[True, True,True])
df.head()

