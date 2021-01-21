#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import os.path
import shutil
import subprocess


# In[2]:


os.getcwd()


# In[3]:


path = r"C:\Users\Purushotham\Desktop\oracle\day_04\data"
os.chdir(path)
os.getcwd()


# In[4]:


files = os.listdir()
print(files)


# In[8]:


os.path.splitext('data1.txt')[1][1:]


# In[10]:


exts = []
for file in files:
    exts.append(os.path.splitext(file)[1][1:])
print(exts)


# In[11]:


dirs = set(exts)
print(dirs)


# In[12]:


for dir in dirs:
    os.mkdir(dir)


# In[15]:


src  = os.path.join(path, "data1.txt")
dest = os.path.join(path, "txt", "data1.txt")
print(src)
print(dest)


# In[18]:


for file in files:
    src = os.path.join(path, file)
    ext = os.path.splitext(file)[1][1:]
    dest = os.path.join(path, ext, file)
    shutil.move(src, dest)


# In[ ]:




