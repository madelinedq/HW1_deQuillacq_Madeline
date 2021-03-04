#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[5]:


np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])


# In[25]:


import numpy as np
numbers = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
type(numbers)
numbers
np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])


# In[7]:


x_integer_array = np.arange(1,7)
type(x_integer_array)
x_integer_array


# In[8]:


y_integer_array = np.arange(5,11)
type(y_integer_array)
y_integer_array


# In[26]:


import matplotlib
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 2, 3, 4, 5, 6])
ypoints = np.array([5, 6, 7, 8, 9, 10])

plt.plot(xpoints, ypoints)
plt.show()


# In[11]:


import matplotlib.pyplot as plt
import numpy as np

x = np.array([0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0])
y1 = np.array([1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0])
y2 = np.array([5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0])
y3 = np.array([9.0, 9.5, 10.0, 10.5, 11.0, 11.5, 12.0, 12.5, 13.0])

plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)

plt.xlabel("X Label")
plt.ylabel("Y Label")

plt.show()


# In[24]:


import matplotlib.pyplot as plt
import numpy as no

x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = np.array([0, 1.5, 3, 4.5, 6, 7.5, 9, 10.5, 12, 13.5, 15])

plt.subplot(2, 2, 1)
plt.plot(x,y)

x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = np.array([5, 11, 7, 4, 15, 4, 16, 6, 13, 2, 17])

plt.subplot(2, 2, 2)
plt.plot(x,y)

x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = np.array([5, 6, 7, 6, 5, 6, 7, 6, 5, 6, 7])

plt.subplot(2, 2, 3)
plt.plot(x,y)

x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = np.array([2, 3, 2, 4, 6, 5, 8, 7, 10, 9, 14])

plt.subplot(2, 2, 4)
plt.plot(x,y)

plt.show()


# In[ ]:




