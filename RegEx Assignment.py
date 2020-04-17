#!/usr/bin/env python
# coding: utf-8

# In[2]:


import re


# In[3]:


#1. Write a code to find out all email ids from following string:
#abc = 'ideators@google.com, career@hotmail.com, users@yahoo-mail.com'
abc = 'ideators@google.com, career@hotmail.com, users@yahoo-mail.com'
emails = re.findall(r'[\w\.-]+@[\w\.-]+', abc)
for email in emails: 
    print(email)


# In[4]:


#2. Find phone numbers starting from +44 from my str given in classroom
mystr = '''Tata Limited
Dr. David Landsman, executive director
18, Grosvenor Place
London SW1X 7HSc
Phone: +44 (20) 7235 8281
Fax: +44 (20) 7235 8727
Email: tata@tata.co.uk
Website: www.europe.tata.com
Directions: View map

Tata Sons, North America
1700 North Moore St, Suite 1520
Arlington, VA 22209-1911
USA
Phone: +1 (703) 243 9787
Fax: +1 (703) 243 9791
66-66
455-4545
Email: northamerica@tata.com
Website: www.northamerica.tata.com
Directions: View map fass

bahut hi badia aadmi haiaiinaiiiiiiiiiiii'''
patt=re.compile(r'\+44')
matches=patt.finditer(mystr)
for match in matches:
    print(match)


# In[5]:


#3. Extract website name from  str given in classroom
patt=re.compile(r'(//|\s+|^)(\w\.|\w[A-Za-z0-9-]{0,61}\w\.){1,3}[A-Za-z]{2,6}')
matches=patt.finditer(mystr)
for match in matches:
    print(match)


# In[ ]:




