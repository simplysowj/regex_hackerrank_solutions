#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Detect floating point number
import re
if __name__ == "__main__":
    t = int(input().strip())
    pattern = '^[+-]?[0-9]*\.[0-9]+$'
    
    for _ in range(t):
        print(bool(re.match(pattern, input())))
        
    


# In[ ]:





# In[ ]:




