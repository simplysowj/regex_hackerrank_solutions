#!/usr/bin/env python
# coding: utf-8

# You are given some input, and you are required to check whether they are valid mobile numbers.
# 
# A valid mobile number is a ten digit number starting with a 7,8 or 9 .
# 
# Concept
# 
# A valid mobile number is a ten digit number starting with a 7,8 or 9 .
# 
# Regular expressions are a key concept in any programming language. A quick explanation with Python examples is available here. You could also go through the link below to read more about regular expressions in Python.

# In[1]:


import re
def val_phone():
    n=int(input())
    pattern="^[789]"
    for i in range(n):
        number=(input())
        if len(number)==10 and number.isdigit():
            ans=re.findall(pattern,number)
            if len(ans)==1:
                print ("YES")
            else:
                print ("NO" )  
        else:
            print ("NO")            


val_phone()  

