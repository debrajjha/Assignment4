#!/usr/bin/env python
# coding: utf-8

# # Write a Python program to create a lambda function that adds 25 to a given number passed in as an argument.

# In[1]:


x=int(input("Enter a number:"))
y= lambda x:x+25
print(y(x))


# # Write a Python program to triple all numbers of a given list of integers. Use Python map.
# 
# 

# In[2]:


x=eval(input("Enter list's number:"))
l=list(map(lambda x:x*3,x))
print("Triple of list numbers:",l)


# # Write a Python program to square the elements of a list using map() function.

# In[3]:


x=eval(input("Enter list's number:"))
l=list(map(lambda x:x**2,x))
print("Square the elements of the list:",l)


# In[ ]:




