#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


# Recorrer una lista 
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)


# In[3]:


# Recorrer una cadena
for x in "banana":
  print(x)


# In[4]:


# Recorrer una tuple (immutable)
fruits = ("apple", "banana", "cherry")
for i in fruits:
    print(i)


# In[5]:


# Recorrer un diccionario  
d = dict() 
d['xyz'] = 123
d['abc'] = 345
for i in d :
    print("%s  %d" %(i, d[i]))


# In[6]:


# Parar el bucle dada una condición. The break Statement

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana": 
    break # Termina la ejecución del bucle cuando se da la condición fruits (x) == "banana". Sólo se ejecuta, si se cumple esa condición


# In[7]:


# Termina la ejeción antes de visualizar el resultado
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "cherry":
    break
  print(x)


# In[8]:


# Saltar un ciclo del bucle cuando se da una condición.
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)


# In[9]:


# Ejecutar un número dado de iteraciones/ciclos range(valor numérico)
for x in range(6): # IMPORTANTE: range(6) no son los valores de 0 a 6, sino de 0 a 5.
  print(x)


# In[10]:


fruits = ["apple", "banana", "cherry"]

numero_de_elementos = len(fruits) # len == Número de elementos que contiene el array

for x in range(numero_de_elementos):
  print(x)


# In[11]:


fruits = ["apple", "banana", "cherry"]

numero_de_elementos = len(fruits) # len == Número de elementos que contiene el array

for x in range(numero_de_elementos):
  print(fruits[x]) # Accedemos a los elementos del array uno a uno, en un bucle


# In[12]:


# Podemos indicar a range el punto de partida
for x in range(2, 6):
  print(x)


# In[13]:


# También podemos indicar a range el tamaño del paso por ciclo. En este caso, de 3 en 3.
for x in range(2, 30, 3):
  print(x)


# ### Bucles anidados
#  
# ### ¡MUY IMPORTANTES!

# In[14]:


adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y) 


# ### Ejercicio 1
#  
# Realiza un bucle for que recorra las tres listas generando un listado como:
#  
# 1 red apple
#  
# 2 red apple
#  
# 3 red apple
#  
# 1 red banana
#  
# 2 red banana
#  
# 3 red banana
#  
# 1 red cherry
#  
# 2 red cherry
#  
# Etc.

# In[55]:


numbers = [1,2,3]
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

# Respuesta
for x in adj: 
    for y in fruits: 
        for z in numbers: 
            print(z, x, y)


# ### Ejercicio 2
# 
# Recorre y muestra todos los elementos de la siguiente lista

# In[15]:


a = [[2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20]] 

# Respuesta
for list in a:
    for x in list:
        print (x)


# ### Ejercicio 3
# Recorre y muestra todos los elementos del siguiente diccionario.
#  
# Solución: abc
# 1
# 2
# 3
# efg
# Clave

# In[42]:


# Respuesta
diccionario = {'abc':[1,2,3], 'efg':{'Clave':'Mundo'}}

for x in diccionario:
    print(x)
    for y in diccionario[x]:
        print(y)


# ### Ejercicio 4
# Usando bucles for, muestra la suma de los elementos de cada fila de la lista. Es decir: 30, 45 y 60.

# In[16]:


a = [[2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20]] 

# Respuesta
for x in range(0,len(a)):
    for y in range(0,len(a[x])):
        z = sum (a[x])
        
    print(z)


# ### El bucle `while`
#  
# Es similar a for, pero en este caso el bucle puede ser ascendente o descendente, dependiendo de la condición. Ej.: i < 6, se lee: "mientras i sea menor que 6"

# In[ ]:


i = 1
while i < 6:
  print(i)
  i += 1 # También i = i + 1, para incrementar el calor de i en cada ciclo y vaya acercándose de 1 en 1 al valor de control (6)


# In[ ]:


# Usando `break` para interrunpir el bucle
i = 1
while i < 6:
  print(i)
  if i == 3:
    break # Cuando i = 3, se interrumpe el bucle.
  i += 1 


# ### Ejercicio 5
#  
# Construye un bucle while que muestre cada fila de la lista a

# In[38]:


a = [ [2, 4, 6, 8 ],  
    [ 1, 3, 5, 7 ],  
    [ 8, 6, 4, 2 ],  
    [ 7, 5, 3, 1 ] ]  

# Respuesta (II). Otra posible solución
i=1
while i < 5:
    print (a[i-1])
    i+=1


# In[40]:


a = [ [2, 4, 6, 8 ],  
    [ 1, 3, 5, 7 ],  
    [ 8, 6, 4, 2 ],  
    [ 7, 5, 3, 1 ] ]  

# Respuesta (I)
i = 0 
while i < len(a): 
    print(a[i])
    i += 1


# ### Funciones

# In[18]:


# 1) Creamos la función con el operador "def"
def funcionEjemplo():
  print('Hola')

# 2) POSTERIORMENTE, llamamos a la función en el punto donde queremos que se ejecute.
funcionEjemplo() # Una vez que la función se ha construido, ha de ser llamada expresamente en el código


# Funciones que reciben parámetro al ser llamadas

# In[19]:


# 1) Creamos la función con el operador "def"
def funcionEjemplo(a, b): # a y b, son parámetros de entrada. Se pueden llamar con cualquier nombre válido
  print('suma de a y b:', a+b)

# 2) POSTERIORMENTE, llamamos a la función en el punto donde queremos que se ejecute.

funcionEjemplo(1,2) # Llamamos a la función con los parámetros que ha de usar. Aquí a=1, b=2


# ### Ejercicio 6
#  
# Crea una función que reciba como parámetro la lista `a` y muestre la suma de los elementos de cada fila de la lista "a".
#  
# Ej.: funcion_2(a)

# In[32]:


a = [[2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20]] 

# Respuesta
def funcion_1(lista):
    
    
    for x in range(0, len(lista)):
        for y in range(0,len (lista[x])):
            z = sum(lista[x])
        print (z)
        
print(funcion_1(a))


# ### Cláusulas condicionales e if ... else statements

# ### Cláusulas condicionales
#     Equals: a == b
#     Not Equals: a != b
#     Less than: a < b
#     Less than or equal to: a <= b
#     Greater than: a > b
#     Greater than or equal to: a >= b
# 

# In[ ]:


a = 33
b = 200
if b > a:
  print("b > a")
else:
  print("a > b")


# In[ ]:


a = 330
b = 200
if b > a:
  print("b > a")
else:
  print("a > b")


# In[ ]:


a = 33
b = 200
if b == a:
  print("b = a")
else:
  print("a != b")


# In[ ]:


a = 33
b = 33
if b == a:
  print("b = a")
else:
  print("a != b")


# ### Ejercicio 7
#  
# Repite la función del ejercicio 6, pero ahora visualiza sólo los valores mayores de 35 y sino, que imprima 'suma menor de 35'

# In[39]:


a = [[2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20]] 

# Respuesta
def funcion_1(lista):
    
    
    for x in range(0, len(lista)):
        for y in range(0,len (lista[x])):
            z = sum(lista[x])
        if z > 35:
            print(z)
        else:
            print("Suma menor que 35")
        
print(funcion_1(a))

