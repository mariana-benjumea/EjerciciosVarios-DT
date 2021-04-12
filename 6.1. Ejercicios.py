#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


np.__version__


# In[3]:


#numpy es 10 a 100 veces mas rápido de python
my_arr = np.arange(10000)
my_list = list(range(10000))


# In[6]:


get_ipython().run_line_magic('time', 'for _ in range(10): my_arr2 = my_arr * 2')


# In[10]:


# vamos a trabajar con arrays (que vienen siendo matrices)


# In[11]:


# (filas , columnas)
data = np.random.randn(2,3)


# In[12]:


data


# In[13]:


data*2


# In[18]:


#este comando y el siguiente significan lo mismo, que es elevar al cuadrado
data**2


# In[19]:


np.power(data,2)


# In[21]:


data2 = range (3)


# In[34]:


data2=[1,2,3]


# In[35]:


data2


# In[36]:


#elevar data a la data2
np.power(data,data2)


# In[38]:


#fila por columna 
data.dot(data2)


# In[ ]:


data3=[4,5,6]


# # Lógica

# In[39]:


a = np.array ([1,1,0,0], dtype=bool)
b = np.array ([1,0,1,0], dtype=bool)


# In[40]:


# o logica
np.logical_or(a,b)


# In[44]:


# and logica
np.logical_and(a,b)


# In[51]:


a = np.arange(9).reshape(3,3)


# In[46]:


a


# In[60]:


#triangular superior
np.triu([[1,2,3],[4,5,6],[7,8,9],[10,11,12]],-1)


# In[55]:


#triangular inferior
np.tril([[1,2,3],[4,5,6],[7,8,9],[10,11,12]],-1)


# # creación de arrays a partir de objetos tipo lista

# In[62]:


data1 = [1,2,3,4,5]


# In[63]:


arr1 = np.array(data1)


# In[64]:


arr1


# In[65]:


data1


# In[75]:


#lista de listas
data2 = [[1,2,3,4,5], [6,7,8,9,10]]


# In[76]:


data2


# In[77]:


arr2 = np.array(data2)


# In[79]:


arr2 #las listas deben tener las mismas dimensiones para obtener el array


# In[80]:


arr2.dtype


# In[87]:


#pasar a float
float_arr2 = arr2.astype(np.float64)


# In[84]:


arr2


# In[86]:


float_arr2


# In[93]:


#pasar a string
string_arr2 = arr2.astype(np.string_)


# In[94]:


string_arr2


# In[95]:


#pasar a unicode
unicode_arr2 = arr2.astype(np.unicode_)


# In[96]:


unicode_arr2


# In[97]:


#pasar a int
integer_arr2 = arr2.astype(np.int32)


# In[98]:


integer_arr2


# In[99]:





# In[100]:


arr = a(10)


# In[ ]:




