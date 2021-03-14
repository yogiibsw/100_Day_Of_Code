#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install seaborn


# In[2]:


pip install git+https://github.com/mwaskom/seaborn.git


# In[3]:


import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[4]:


sns.set_theme(color_codes=True)


# In[5]:


tips = sns.load_dataset("tips")


# In[6]:


sns.regplot(x="total_bill", y="tip", data=tips);


# In[7]:


sns.lmplot(x="total_bill", y="tip", data=tips);


# In[8]:


sns.lmplot(x="size", y="tip", data=tips);


# In[9]:


sns.lmplot(x="size", y="tip", data=tips, x_jitter=.05);


# In[10]:


sns.lmplot(x="size", y="tip", data=tips, x_estimator=np.mean);


# In[11]:


anscombe = sns.load_dataset("anscombe")


# In[12]:


sns.lmplot(x="x", y="y", data=anscombe.query("dataset == 'I'"),
           ci=None, scatter_kws={"s": 80});


# In[13]:


sns.lmplot(x="x", y="y", data=anscombe.query("dataset == 'II'"),
           ci=None, scatter_kws={"s": 80});


# In[14]:


sns.lmplot(x="x", y="y", data=anscombe.query("dataset == 'II'"),
           order=2, ci=None, scatter_kws={"s": 80});


# In[15]:


sns.lmplot(x="x", y="y", data=anscombe.query("dataset == 'III'"),
           ci=None, scatter_kws={"s": 80});


# In[ ]:




