#!/usr/bin/env python
# coding: utf-8

# In[57]:


# Importing all the Required Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import datetime as dt
import warnings
plt.style.use('dark_background')
from plotly.offline import init_notebook_mode
init_notebook_mode(connected=True)
warnings.filterwarnings('ignore')
pd.set_option('display.max_columns',None)
import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))


# In[58]:


df=pd.read_csv('Life Expectancy Data.csv')
df.head()


# In[59]:


# Size of the data 
df.shape


# In[60]:


# A Quick Information about the Data
df.info()


# In[61]:


# Checking for Null Values
df.isnull().sum()


# In[63]:


# Replacing the Null Values with mean values of the data
from sklearn.impute import SimpleImputer
imputer=SimpleImputer(missing_values=np.nan,strategy='mean',fill_value=None)
df['Life expectancy ']=imputer.fit_transform(df[['Life expectancy ']])
df['Adult Mortality']=imputer.fit_transform(df[['Adult Mortality']])
df['Alcohol']=imputer.fit_transform(df[['Alcohol']])
df['Hepatitis B']=imputer.fit_transform(df[['Hepatitis B']])
df[' BMI ']=imputer.fit_transform(df[[' BMI ']])
df['Polio']=imputer.fit_transform(df[['Polio']])
df['Total expenditure']=imputer.fit_transform(df[['Total expenditure']])
df['Diphtheria ']=imputer.fit_transform(df[['Diphtheria ']])
df['GDP']=imputer.fit_transform(df[['GDP']])
df['Population']=imputer.fit_transform(df[['Population']])
df['thinness  1-19 years']=imputer.fit_transform(df[['thinness  1-19 years']])
df['thinness 5-9 years']=imputer.fit_transform(df[['thinness 5-9 years']])
df['Income composition of resources']=imputer.fit_transform(df[['Income composition of resources']])
df['Schooling']=imputer.fit_transform(df[['Schooling']])


# In[64]:


df.isnull().sum()


# In[65]:


df.describe()


# In[66]:


df.head()


# In[67]:


df.corr().head()


# In[68]:


plt.figure(figsize=(15,10))
sns.heatmap(df.corr(),annot=True,cmap='Greens')
plt.show()


# In[69]:


fig=px.histogram(df,x='Life expectancy ',template='plotly_dark')
fig.show()


# <b> DEVELOPED COUNTRIES HAS MAXIMUM LIFE EXPENTANCY

# In[71]:


fig=px.violin(df,x='Status',y='Life expectancy ',color='Status',template='plotly_dark',box=True,title='Life expectancy Based on Countries status')
fig.show()


# In[72]:


fig=px.line(df.sort_values(by='Year'),x='Year',y='Life expectancy ',animation_frame='Country',animation_group='Year',color='Country',markers=True,template='plotly_dark',title='<b> Country wise Life Expectancy over Years')
fig.show()


# In[73]:


px.scatter(df,y='Adult Mortality',x='Life expectancy ',color='Country',size='Life expectancy ',template='plotly_dark',opacity=0.6,title='<b> Life Expectancy Versus Adult Mortality')


# In[74]:


px.scatter(df,x='Life expectancy ',y='percentage expenditure',color='Country',size='Year',template='plotly_dark',title='<b> Life Expectancy Versus Percentage expenditure')


# #### DECREASE IN INFANT DEATHS INCREASES LIFE EXPECTANCY

# In[75]:


px.scatter(df.sort_values(by='Year'),y='infant deaths',x='Life expectancy ',template='plotly_dark',size='Year',color='Country',opacity=0.6,title='<b>Life Expectancy Versus Infant Deaths of Countries in every Year')


# In[76]:


px.scatter_3d(df.sort_values(by='Year'),y='Schooling',x='Life expectancy ',z='Total expenditure',template='plotly_dark',color='Country',size='Total expenditure')


# In[77]:


px.scatter_3d(df.sort_values(by='Year'),y='Adult Mortality',x='Life expectancy ',z='infant deaths',size='Life expectancy ',template='plotly_dark',color='Country')


# In[78]:


px.scatter(df.sort_values(by='Year'),y='Schooling',x='Life expectancy ',animation_frame='Year',animation_group='Country',template='plotly_dark',color='Country',size='Life expectancy ',title='<b> Life expectancy versus Schooling of countries in every year')


# In[29]:


px.scatter(df.sort_values(by='Year'),y='Adult Mortality',x='Life expectancy ',animation_frame='Year',animation_group='Country',color='Country',size='Life expectancy ',opacity=0.6,template='plotly_dark',title='<b> Life Expectancy Versus Adult Mortality in every year')


# In[79]:


px.scatter(df.sort_values(by='Year'),y=' BMI ',x='Life expectancy ',animation_frame='Year',animation_group='Country',template='plotly_dark',color='Country',size='Life expectancy ',opacity=0.6,title='<b> Life expectancy versus BMI of Countries in every Year')


# In[80]:


px.scatter(df.sort_values(by='Year'),y='GDP',x='Life expectancy ',animation_frame='Year',animation_group='Country',template='plotly_dark',color='Country',size='Life expectancy ',title='<b>Life Expectancy Versus GDP of Countries in every Year')

