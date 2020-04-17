#!/usr/bin/env python
# coding: utf-8

# # Pillow Assignment

# In[1]:


from PIL import Image


# In[2]:


# 1)
image = Image.open('flowernew1.jpg')
logo = Image.open('image_thumbnail.jpg')
image_copy1 = image.copy()
#position1 = ((image_copy1.width - logo.width), (image_copy1.height - logo.height))
image_copy1.paste(logo, (130,0))
image_copy1


# In[3]:


#2)
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import requests
raw_data=requests.get('https://picsum.photos/500/500?random')
name='image.png'
with open(name,'wb')as x:
    x.write(raw_data.content)
image=Image.open(name)
draw=ImageDraw.Draw(image)
fontx=ImageFont.truetype('arial',55)
draw.text((100,100),"Hello Pillow",(255,0,0),font=fontx)
draw.line(xy=[(0,0),(500,0)],fill='black',width=30)
draw.line(xy=[(0,0),(0,500)],fill='black',width=20)
draw.line(xy=[(500,0),(500,500)],fill='black',width=25)
draw.line(xy=[(0,500),(500,500)],fill='black',width=45)


# In[4]:


image


# In[ ]:




