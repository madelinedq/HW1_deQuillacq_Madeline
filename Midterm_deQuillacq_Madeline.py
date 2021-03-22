#!/usr/bin/env python
# coding: utf-8

# In[17]:


def Count_Frequency(my_dict): 
  
    freq = {} 
    for item in my_dict: 
        if (item in freq): 
            freq[item] += 1
        else: 
            freq[item] = 1
  
    for key, value in freq.items(): 
        print ("% d : % d"%(key, value)) 
   
    print('Explanation:')
    for key, value in freq.items():
        print('Here % d occurs % d times'%(key, value))
  
if __name__ == "__main__":  
    my_dict =[2,4,6,8,4,5,2,1,9,0,4,6,7,4,3,2,1,9,10,3,7,9,6,0,1,3,5,6,7,8,9,10,2,3,6,8,9,10,6,7,4,3] 
  
    Count_Frequency(my_dict)


# In[15]:


import matplotlib.pyplot as plt
import numpy as np

dict = [2,4,6,8,4,5,2,1,9,0,4,6,7,4,3,2,1,9,10,3,7,9,6,0,1,3,5,6,7,8,9,10,2,3,6,8,9,10,6,7,4,3]
freq = {}
for item in dict:
    if (item in freq):
        freq[item] += 1
    else:
        freq[item] = 1
keys = freq.keys()
values = freq.values()
plt.bar(keys, values)
plt.title("Frequencies")


# In[6]:


import json

dict = [2,4,6,8,4,5,2,1,9,0,4,6,7,4,3,2,1,9,10,3,7,9,6,0,1,3,5,6,7,8,9,10,2,3,6,8,9,10,6,7,4,3]
freq = {}
for item in dict:
    if (item in freq):
        freq[item] += 1
    else:
        freq[item] = 1


y = json.dumps(freq, indent = 4)


with open("./output.json", "w") as out:
   json.dump(freq, out)
    
print (y) 


# In[21]:


import pandas as pd

df = pd.read_json('your_posts_1.json')
df.head(3)


# In[22]:


df.rename(columns={'timestamp': 'date'}, inplace=True)

df = df.drop(['attachments', 'title', 'tags'], axis=1)

pd.to_datetime(df['date'])

df.head(3)


# In[23]:


print(df.shape)
df.tail(3)


# In[24]:


df = df.set_index('date')
post_counts = df['data'].resample('MS').size()
post_counts


# In[30]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df.rename(columns={'data': 'Number of Posts'}, inplace=True)

sns.set(rc={'figure.figsize':(40,20)})
sns.set(font_scale=3)

x_labels = post_counts.index

sns.barplot(x_labels, post_counts, color='purple')

tick_positions = np.arange(10, len(x_labels), step=24)

plt.xticks(tick_positions, x_labels[tick_positions].strftime("%Y"))

plt.title('Madeline Monthy FaceBook Posts')

plt.show()


# In[6]:





# In[ ]:




