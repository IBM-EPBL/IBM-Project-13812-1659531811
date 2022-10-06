#!/usr/bin/env python
# coding: utf-8

# ## 1.Split this String

# In[1]:


s="Hi there sam!"
v=s.split()
print(v)


# ## 2.Use .format()to print the following String

# In[5]:


plant ="Earth"
diameter ="12742"
v="The diameter of Earth is {an} kilometer"
print(v.format(an=12742))


# ## 3.In this nest dictionary grab the word "hello

# In[1]:


d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
print(d['k1'][3]["tricky"][3]['target'][3])


# ## 5.Create an array of all the even integers from 20 to 35

# In[10]:


import numpy as np
array=np.arange(20,35,2)
print("Array =",array)


# ## 6. Create a 3x3 matrix with value ranging from 0 to 8

# In[17]:


import numpy as np
x =  np.arange(0, 9)
print(x.reshape(3,3))


# ## 7. Concatenate a and b 

# In[6]:


import numpy as np

a = np.array([1, 2, 3])

b = np.array([4, 5, 6])

v = np.concatenate((a, b))

print(v)


# ## 8.Create a dataframe with 3 rows and 2 columns

# In[17]:


import pandas as pd

data = {
  "x": [1,2,3],
  "y": [4,5,6]
}
df = pd.DataFrame(data)

print(df) 


# ## 9.Generate the series of dates from 1st Jan,2023 to 10th Feb 2023

# In[11]:


import pandas as pd
a= pd.date_range(start='2023-01-01', end='2023-02-10')
print(a)


# ## 10.Create 2D list to data frame

# In[8]:


import pandas as pd
import numpy as np
lists = [[1, 'aaa', 22], [2, 'bbb', 25], [3, 'ccc', 24]]
v=pd.DataFrame(lists)
print(v)

