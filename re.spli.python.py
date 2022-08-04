#!/usr/bin/env python
# coding: utf-8

# In[1]:


regex_pattern = r"[.,]+"	# Do not delete 'r'.

import re
print("\n".join(re.split(regex_pattern, input())))


# In[ ]:




