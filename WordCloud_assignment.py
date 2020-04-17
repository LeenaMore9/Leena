#!/usr/bin/env python
# coding: utf-8

# ## WordCloud_assignment
# 

# In[1]:


import numpy as np
from matplotlib import pyplot as plt
from wordcloud import WordCloud,STOPWORDS


# In[2]:


from PIL import Image
image=Image.open("alice_mask.png")
image


# In[3]:


alice_mask=np.array(Image.open("alice_mask.png"))
alice_mask


# In[4]:


def transform_format(val):
    if val==0:
        return 255
    else:
        return val


# In[5]:


new= open ("alice_novel.txt","r") 
text=new.read()


# In[6]:


transformed_alice_mask=np.ndarray((alice_mask.shape[0],alice_mask.shape[1]),np.int32)
for i in range(len(alice_mask)):
    transformed_alice_mask[i]=list(map(transform_format,alice_mask[i]))


# In[7]:


transformed_alice_mask


# In[8]:


wc=WordCloud(background_color="white",max_words=1000,mask=transformed_alice_mask,
    contour_width=3,contour_color='firebrick').generate(text)


# In[9]:


plt.figure(figsize=[20,10])
plt.imshow(wc,interpolation='bilinear')
plt.axis("off")
plt.show()


# In[ ]:




