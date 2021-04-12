#!/usr/bin/env python
# coding: utf-8

# ### **Instrucciones**
#  
# * Dispones de 60 minutos para realizar el examen
# * Lee atentamente las instrucciones
# * Contesta a cada pregunta siguiendo las instrucciones que se indican para su realización

# ### Ejercicio 1 (puntuación 0.5)
#  
# Mediante un bucle **`for`** suma los dos primeros elementos de la lista y por otro lado los dos últimos.
#  
# ---- Respuesta ---------
# * (1+2=3)
# * (4+5=9)

# In[2]:


intLista =[1, 2, 3, 4, 5]

# Respuesta
for x in intLista:
    if x == 1 or x == 3 or x == 4:
        continue
    else:
        y = x-1+x
        print(y)


# ### Ejercicio 2 (puntuación 1)
#  
# Por medio de un bucle, cuenta:
#  
# * El número de letras de la frase
# * El número de palabras de la frase
# * El número de los espacios en blanco de la frase
#  
# ----- Respuesta -------
# * Letras:  19
# * Palabras:  5
# * Espacios en blanco:  4

# In[147]:


Frase = 'Esto es sólo una prueba'

# Respuesta
l = 0
p = 0
e = 0

for x in Frase:
    if(x != " "):
        l += 1
    elif(x == " "):
        e += 1

for y in Frase.split(" "):
    p += 1
    
print("Letras:", l)
print("Palabras:", p)
print("Espacios en blanco:", e)


# ### Ejercicio 3 (puntuación 1)
#  
# Por medio de un bucle, cuenta:
#  
# * Las letras de la frase
# * Las palabras de la frase
# * Los espacios en blanco de la frase
#  
# -------- Respuesta ------------
# * Letras:  19
# * Palabras:  5
# * Espacios en blanco:  6

# In[148]:


Frase = 'Esto es sólo  una  prueba'

# Respuesta
l = 0
p = 0
e = 0

for x in Frase:
    if(x != " "):
        l += 1
    elif(x == " "):
        e += 1

for y in Frase.split(" "):
    p += 1
    
print("Letras:", "  ", l)
print("Palabras:", "  ", p)
print("Espacios en blanco:", "  ", e)


# ### Ejercicio 4 (puntuación 1)
#  
# Por medio de un bucle **`while`** imprime la frase en orden inverso.

# In[149]:


Frase = 'Esto es sólo una prueba'

# Respuesta
x = 0 

while x < len(Frase):
    x += 1
    print(Frase[-x])


# ### Ejercicio 5 (puntuación 1)
#  
# Mediante bucles `while` genera la siguiente lista de palabras:
#  
# adj = ["red", "big", "tasty"]
#  
# fruits = ["apple", "banana", "cherry"]
#  
# ------- Respuesta ----------
# * tasty : cherry
# * tasty : banana
# * tasty : apple
# * big : cherry
# * big : banana
# * big : apple
# * red : cherry
# * red : banana
# * red : apple

# In[130]:


adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

# Respuesta
i = 0
j = 0

while i < len(adj):
    while j < len(fruits):
        print(adj[i], ":", fruits[j])
        j+= 1
    j = 0
    i += 1


# ### Ejercicio 6 (puntuación: 0,5)
#  
# Mediante bucles `for` genera la siguiente lista de palabras:
#  
# adj = ["red", "big", "tasty"]
#  
# fruits = ["apple", "banana", "cherry"]
#  
# ------- Respuesta ----------
# * tasty : cherry
# * tasty : banana
# * tasty : apple
# * big : cherry
# * big : banana
# * big : apple
# * red : cherry
# * red : banana
# * red : apple

# In[126]:


adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

# Respuesta
for x in reversed(adj):
    for y in reversed(fruits):
        print(x, ":", y) 


# ### Ejercicio 7 (puntuación: 1)
#  
# Mediante un bucle `for in-line` calcula el cuadrado de los números 2 al 10. Ambos inclusive
#  
# --------- Respuesta -----------
#  
# [4, 9, 16, 25, 36, 49, 64, 81, 100]

# In[151]:


# Respuesta
cuadrado= range(2,11)
[x**2 for x in rango]


# ### Ejercicio 8 (puntuación 1)
#  
# Para el mismo conjunto de datos del ejercicio anterior, mediante **bucles for in-line**, genera una lista de tuplas tal como este:
# * [('red', 'apple'),
# * ('red', 'banana'),
# * ('red', 'cherry'),
# * ('big', 'apple'),
# * ('big', 'banana'),
# * ('big', 'cherry'),
# * ('tasty', 'apple'),
# * ('tasty', 'banana'),
# * ('tasty', 'cherry')]

# In[99]:


adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

# Respuesta
[print((adjetivo, fruta)) for adjetivo in adj for fruta in fruits]


# ### Ejercicio 9 (puntuación 1)
#  
# Genera una lista con las letras individuales de la siguiente lista de palabras.
#  
# **Puedes mostrar la lista en horizontal o vertical**, como te sea más fácil
#  
# ----------- Respuesta -----------------
#  
# ['a',
#  'p',
#  'p',
#  'l',
#  'e',
#  'b',
#  'a',
#  'n',
#  'a',
#  'n',
#  'a',
#  'p',
#  'e',
#  'a',
#  'r',
#  't',
#  'h',
#  'e',
#  'h',
#  'e',
#  'l',
#  'l',
#  'o']

# In[104]:


listado = ["apple", "banana", "pear", "the", "hello"]

# Respuesta
x = 0 

while x < len(listado):
    print(listado[x])
    x += 1


# ### Ejercicio 10 (puntuación 1)
#  
# Programa una función que retorne una lista con el máximo y mínimo de la lista/array dado.
#  
# ----------- Respuesta ----------------
#  
# [-20, 73]

# In[118]:


numeros = [7,-20,73,40,5,6,8,-3]

# Respuesta

def num(numeros):
    x=[]
    x.append(min(numeros))
    x.append(max(numeros))
    print(x)
    
num(numeros)


# ### Ejercicio 11 (puntuación 1)
#  
# Programa una función que mediante bucles **`for`**
#  
# retorne una lista con el máximo y mínimo de la lista/array dado.
#  
# ----------- Respuesta ----------------
#  
# [-20, 73]

# In[115]:


numeros = [7,-20,73,40,5,6,8,-3]

# Respuesta

def funcion (numeros):
    mayor = numeros[0]
    menor = numeros[0]
    i = []
    for x in range(len(numeros)):
        if numeros[x]>mayor:
            mayor = numeros[x]
        elif numeros [x]<menor:
            menor = numeros[x]
    i.append(menor)
    i.append(mayor)
    print(i)
    
funcion(numeros)

