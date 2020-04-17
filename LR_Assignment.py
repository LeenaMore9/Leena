#!/usr/bin/env python
# coding: utf-8

# ## LR_Assignment

# In[1]:


import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


# In[2]:


df=pd.read_excel("insurance.xls")


# In[3]:


df


# In[4]:


x=df.iloc[:,:-1].values
x


# In[5]:


Y=df.iloc[:,1].values
Y


# In[6]:


plt.scatter(x,Y,color="red")


# In[7]:


from sklearn.model_selection import train_test_split


# In[8]:


x_train,x_test,Y_train,Y_test=train_test_split(x,Y,test_size=1/3,random_state=0)


# In[9]:


x_train


# In[10]:


x_test


# In[11]:


Y_train


# In[12]:


Y_test


# In[13]:


from sklearn.linear_model import LinearRegression


# In[14]:


regressor=LinearRegression()
regressor.fit(x_train,Y_train)


# In[15]:


y_pred=regressor.predict(x_test)


# In[16]:


y_pred


# In[17]:


plt.scatter(x_test,Y_test,color="red")
plt.plot(x_train,regressor.predict(x_train),color='blue')
plt.title('total payment vs claims')
plt.xlabel('number of claims')
plt.ylabel('total payment for all the claims in thousands of Swedish Kronor')
plt.show()


# In[18]:


from sklearn.metrics import r2_score
r2_score(Y_test,y_pred)


# In[20]:


y_predict=regressor.predict([[13]])
y_predict


# In[ ]:




