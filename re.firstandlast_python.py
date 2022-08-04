#!/usr/bin/env python
# coding: utf-8

# start() & end()
# These expressions return the indices of the start and end of the substring matched by the group.

# Task
# You are given a string S .
# Your task is to find the indices of the start and end of string k in S.
# 
# 

# In[2]:



import re

st = input()
subst = input()

pattern = re.compile(subst)
match = pattern.search(st)
if not match: print('(-1, -1)')
while match:
    print('({0}, {1})'.format(match.start(), match.end() - 1))
    match = pattern.search(st, match.start() + 1)

