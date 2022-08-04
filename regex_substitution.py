#!/usr/bin/env python
# coding: utf-8

# You are given a text of n lines. The text contains && and || symbols.
# Your task is to modify those symbols to the following:
# 
# && → and
# || → or
# Both && and || should have a space " " on both sides.

# In[5]:


import re
n=int(input())
S=""""""
for i in range(n):
    s=""+input()+""
    S+=s
    if i<n-1:
        S+="\n"
        

    
S=re.sub("(?<= )(&&)(?= )",'and',S)
S=re.sub("(?<= )(\|\|)(?= )","or",S)
print(S)


# In[ ]:




