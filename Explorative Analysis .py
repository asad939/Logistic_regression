#!/usr/bin/env python
# coding: utf-8

# In[25]:


#Exploratary analysis of Titanic Data 


# In[26]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


train = pd.read_csv('titanic_train.csv')


# In[4]:


train.head()


# In[6]:


train.isnull()


# In[9]:


sns.heatmap(train.isnull(),yticklabels=False,cbar=False,cmap='viridis')


# In[10]:


#only two columns have missing values Age and Cabin. Cabin coulumn have too much missing values


# In[13]:


sns.set_style('whitegrid')


# In[17]:


sns.set_style('whitegrid')
sns.countplot(x='Survived',data=train,hue='Sex',palette='RdBu_r')


# In[16]:





# In[18]:


sns.distplot(train['Age'].dropna(),kde=False,color='darkred',bins=30)


# In[19]:


train['Age'].hist(bins=30,color='darkred',alpha=0.7)


# In[21]:


sns.countplot(x='SibSp',data=train)


# In[22]:


train['Fare'].hist(color='green',bins=40,figsize=(8,4))


# In[23]:


import cufflinks as cf
cf.go_offline()


# In[27]:


train['Fare'].iplot(kind='hist',bins=30,color='green')


# In[ ]:




