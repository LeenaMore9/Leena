#!/usr/bin/env python
# coding: utf-8

# # ClosuresDecorators_Assignments

# In[1]:


#1)Write code to add multiple int & str
#i)3,4,5=12,                 
def adder(*num):
      sum=0
      for n in num:
        sum=sum+n
      print("sum:",sum)
adder(3,4,5)


# In[2]:


#ii)I,Speak,Python
def adder(*num):
      sum=" "
      for n in num:
        sum=sum+n
      print(sum)
adder("I"," Speak"," Python")


# In[3]:


#2) Write a function to find out which one greatest among (100,300,200)
def largest(num1, num2, num3):
    if (num1 > num2) and (num1 > num3):
        largest_num = num1
    elif (num2 > num1) and (num2 > num3):
        largest_num = num2
    else:
        largest_num = num3
    print("The largest of the 3 numbers is : ", largest_num)
largest(100, 300, 200)


# In[4]:


#3) write a function for 
#   div(2,0)
#   Can't divide by 0!
def divide(a,b):
    return a/b
def decorator(func):
    def wrapper(*args,**kwargs):
        if args[1]==0:
            print("Can't divide by 0!")       
    return wrapper
divide=decorator(divide)
divide(2,0)


# In[ ]:




