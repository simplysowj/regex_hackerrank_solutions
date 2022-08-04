#!/usr/bin/env python
# coding: utf-8

# You and Fredrick are good friends. Yesterday, Fredrick received N credit cards from ABCD Bank. He wants to verify whether his credit card numbers are valid or not. You happen to be great at regex so he is asking for your help!
# 
# A valid credit card from ABCD Bank has the following characteristics:
# 
# ► It must start with a 4,5  or 6 .
# ► It must contain exactly 16 digits.
# ► It must only consist of digits (0-9).
# ► It may have digits in groups of 4, separated by one hyphen "-".
# ► It must NOT use any other separator like ' ' , '_', etc.
# ► It must NOT have 4 or more consecutive repeated digits.

# In[1]:


import re


for _ in range(int(input())):
    num = input()

    a = bool(re.match(r"^[456]\d{15}$", num))
    b = bool(re.match(r"^[456]\d{3}\-\d{4}\-\d{4}\-\d{4}$", num))
    num = num.replace("-", "")
    c = bool(re.match(r"(?!.*(\d)(-?\1){3})", num))
    if (a or b) and c:
        print("Valid")
    else:
        print("Invalid")


# Explanation
# 
# 4123456789123456 : Valid
# 5123-4567-8912-3456 : Valid
# 61234-567-8912-3456 : Invalid, because the card number is not divided into equal groups of 4.
# 4123356789123456 : Valid
# 5133-3367-8912-3456 : Invalid, consecutive digits 3333 is repeating 3 times.
# 5123 - 3567 - 8912 - 3456 : Invalid, because space '  ' and - are used as separators.

# In[ ]:




