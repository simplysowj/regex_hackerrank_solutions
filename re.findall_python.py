#!/usr/bin/env python
# coding: utf-8

# You are given a string s. It consists of alphanumeric characters, spaces andsymbols(+,-).
# Your task : to find  the substrings of s that contains two / more vowels.
# Also, these substrings must lie between two consonants should contain vowels only.

# In[4]:



import re
s=input()
v='aeiou'
c='qwrtypsdfghjklzxcvbnm'
l=re.findall(r'(?<=[%s])([%s]{2,})[%s]'%(c,v,c),s,flags=re.IGNORECASE)
if not l:
    print(-1)
else:
    for i in l:
        print(i)
    


# In[ ]:




