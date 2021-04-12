#!/usr/bin/env python
# coding: utf-8

# # 1

# In[4]:


type(5)
print(3.0-1)


# In[5]:


type(5)


# In[6]:


print(3.0-1)


# # 2

# In[8]:


x + y = 2


# In[9]:


x * x = 2 


# In[10]:


2 = x


# In[1]:


xy = 2


# # 3

# In[2]:


usa_oro = 46
uk_oro = 27
rumania_oro = 1
total_oro = usa_oro + uk_oro + rumania_oro
print(total_oro)
rumania_oro += 1
print(total_oro)


# # 4

# In[46]:


comienzo = "par"
repetir = "aguas"
u = comienzo + (repetir + " ") * 4


# In[47]:


u


# In[50]:


hi = "hola"
name = "ana" 
saludo = hi + name 
print(saludo)


# In[51]:


saludo = hi + " " + name 
print(saludo)


# In[52]:


mucho = hi + (" " + name)*3
print(mucho)


# # 5

# In[2]:


tiempo_trabajo = 15
tiempo_descanso = 8 
print(tiempo_descanso > tiempo_trabajo )
conducir = True
beber = False
ambos = conducir and beber
print(ambos)


# # 6

# In[67]:


x = float(input("Introduce un número para x: "))
y = float(input("Introduce un número para y: "))
if x == y:
    if y != 0:
        print("x / y es", x/y)
elif x < y:
        print("x es pequeño") 
else:
    print("y es pequeño")


# # 7

# In[72]:


pi = 3.14159
radio = 2.2


# In[79]:


area_circulo = pi * (radio*radio)
print(area_circulo)


# # 8

# In[4]:


x = 1
print(x) 
x_str = str(x)
print("mi número favorito es", x, ".", "x=", x)
print(" mi número favorito es ", x_str + "." + "x=" + x_str)
print(" mi número favorito es " + x_str + "." + "x=" + x_str)


# # 9

# In[5]:


text = "5" 
print(5*text) 
num = 5 
print(5*num)


# # 10

# In[116]:


num = int(input("Un número, por favor: ")) 
if num % 2 == 0:
    print("par")
else:
    print("impar")

