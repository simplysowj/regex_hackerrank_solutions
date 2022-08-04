#!/usr/bin/env python
# coding: utf-8

# A valid email address meets the following criteria:
# 
# It's composed of a username, domain name, and extension assembled in this format: username@domain.extension
# The username starts with an English alphabetical character, and any subsequent characters consist of one or more of the following: alphanumeric characters, -,., and _.
# The domain and extension contain only English alphabetical characters.
# The extension is , 1,2 or 3  characters in length.
# Given n pairs of names and email addresses as input, print each name and email address pair having a valid email address on a new line.
# 
# Hint: Try using Email.utils() to complete this challenge. For example, this code:

# In[1]:


import re
import email.utils
for _ in range(int(input())):
    s = input()
    u = email.utils.parseaddr(s)
    if re.search("^[a-z][\w.-]+@[a-z]+\.[a-z]{1,3}$",u[-1],re.I):
        print(s)


# Explanation
# 
# dexter@hotmail.com is a valid email address, so we print the name and email address pair received as input on a new line.
# virus!@variable.:p is not a valid email address because the username contains an exclamation point (!) and the extension contains a colon (:). As this email is not valid, we print nothing.

# In[ ]:




