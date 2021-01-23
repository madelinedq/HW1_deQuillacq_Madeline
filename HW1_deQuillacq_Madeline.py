#!/usr/bin/env python
# coding: utf-8

# In[1]:


colors = ["blue", "purple", "pink", "yellow", "green"]
print(type(colors))
print(colors)


# In[2]:


nums = list(range(30,60,3))
print(nums)


# In[4]:


thisdict = {
    "Sunny": "play",
    "Rainy": "watching TV",
    "Cloudy": "walk"
}
print(thisdict)


# In[8]:


thisdict.update({"snowy": "ski"})
print(thisdict)


# In[29]:


score = 75
if score >=90:
    print("A")
elif score >= 80 and score < 90:
    print("B")
elif score >= 70 and score < 80:
    print("C")
else:
    print("F")


# In[ ]:




