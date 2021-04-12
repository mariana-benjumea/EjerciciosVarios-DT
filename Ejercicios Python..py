#!/usr/bin/env python
# coding: utf-8

# ### Ejercicio 1
#  
# Mediante el uso de bucle encuentra el elemento mayor de la lista
# [1,3,0,5,9,20,-30]

# In[20]:


# Respuesta 1
lista = [1,3,0,5,9,20,-30]

for x in lista:
    a = sorted(lista)
print(a[len(lista)-1])


# In[51]:


# Respuesta 2 
mayor =-50

for x in lista:
    if mayor < x:
        mayor = x
print (mayor)


# In[50]:


# Respuesta 3
num_elementos = len(lista)
mayor = lista[0]

for x in range(num_elementos):
    if lista[x] > mayor:
        mayor = lista[x]
print(mayor)


# ### Ejercicio 2
#  
# Mediante el uso de bucle encuentra el elemento menor de la lista
# [1,3,0,5,9,20,-30]

# In[52]:


# Respuesta 1
lista = [1,3,0,5,9,20,-30]

for x in lista:
    b = sorted(lista)
print(b[0])


# In[53]:


# Respuesta 2
menor=5000
for x in lista:
    if menor > x:
        menor=x
print (menor)


# In[54]:


# Respuesta 3
num_elementos = len(lista)
menor = lista[0]

for x in range(num_elementos):
    if lista[x] < menor:
        menor = lista[x]
print(menor)


# ### Ejercicio 3
#  
# Mediante el uso de bucle **`while`** encuentra el elemento menor de la lista
# [-100,1,3,0,5,9,20,-30]

# In[66]:



lista = [-100,1,3,0,5,9,20,-30]

# Respuesta
menor=lista[0]
i=0
while i<len(lista):
    if lista[i]<menor:
        menor=lista[i]
    i+=1

print(menor)


# ### Ejercicio 4
#  
# Mediante el uso de bucle **`while`** encuentra el elemento mayor de la lista
# [-100,1,3,0,5,9,20,-30]

# In[67]:


lista = [-100,1,3,0,5,9,20,-30]

# Respuesta
mayor=lista[0]
i=0
while i<len(lista):
    if lista[i]>mayor:
        mayor=lista[i]
    i+=1

print(mayor)


# ### Ejercicio 5
#  
# Mediante un bucle `for` `inline`, encuentra los elementos **pares**

# In[65]:


lista = [-100,1,3,0,5,9,20,-30]

# Respuesta
[x for x in lista if (x % 2 == 0)]


# ### Ejercicio 6
#  
# Mediante un bucle `for` `inline`, encuentra los elementos **mayores de 4**

# In[62]:


lista = [-100,1,3,0,5,9,20,-30]

# Respuesta
[i for i in lista if (i > 4)]


# ### Ejercicio 5
#  
# Mediante una función anónima `lambda`, encuentra los elementos **pares**

# In[27]:


lista = [-100,1,3,0,5,9,20,-30]

# Respuesta

respuesta = list(filter(lambda x : (x % 2 == 0), lista))
print(respuesta)


# ### Ejercicio 5
#  
# Mediante una función , encuentra los elementos **pares**

# In[49]:


lista = [-100,1,3,0,5,9,20,-30]

#Respuesta
def respuesta(y):
    for x in y:
        if x % 2 == 0:
    print(x)

respuesta(lista)


# ### Ejercicio 6
#  
# Mediante una función concatena los elementos de una lista para formar una frase.["Hola,", "esto", "es", "una", "prueba"]
#  
# `Hola, esto es una prueba `

# In[44]:


lista_cadenas = ["Hola,", "esto", "es", "una", "prueba"]

# Respuesta
def respuesta2(y):
    for x in y:
        print(x, end=" ")

respuesta2(lista_cadenas)


# In[ ]:


lista_cadenas = ["Hola,", "esto", "es", "una", "prueba"]

# Respuesta 2

def respuesta

