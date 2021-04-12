#!/usr/bin/env python
# coding: utf-8

# Realiza una función llamada area_rectangulo(base, altura) que devuelva el área del rectangulo a partir de una base y una altura. Calcula el área de un rectángulo de 15 de base y 10 de altura:

# In[1]:


def area (b, a):
    return (b*a)

area(15, 10)


# Realiza una función llamada area_circulo(radio) que devuelva el área de un círculo a partir de un radio. Calcula el área de un círculo de 5 de radio:
# 
# 
# El área de un círculo se obtiene al elevar el radio a dos y multiplicando el resultado por el número pi. Puedes utilizar el valor 3.14159 como pi o importarlo del módulo math:
# 
# import math
# 
# print(math.pi)

# In[2]:


import math

print(math.pi)


# In[6]:


def area_circulo (r):
    return ((r**2)*math.pi)

area_circulo(5)


# Realiza una función llamada relacion(a, b) que a partir de dos números cumpla lo siguiente:
# 
# - Si el primer número es mayor que el segundo, debe devolver 1.
# - Si el primer número es menor que el segundo, debe devolver -1.
# - Si ambos números son iguales, debe devolver un 0.
# 
# 
# Comprueba la relación entre los números: '5 y 10', '10 y 5' y '5 y 5'.

# In[10]:


def relacion (a, b):
    if a > b:
        print (1)
    elif a < b:
        print (-1)
    else:
        print (0)
        
relacion (5, 10)


# Realiza una función llamada intermedio(a, b) que a partir de dos números, devuelva su punto intermedio. Cuando lo tengas comprueba el punto intermedio entre -12 y 24:

# In[12]:


def intermedio (a, b):
    return ((a+b)/2)

intermedio (-12, 24)


# Realiza una función llamada recortar(numero, minimo, maximo) que reciba tres parámetros. El primero es el número a recortar, el segundo es el límite inferior y el tercero el límite superior. 
# 
# La función tendrá que cumplir lo siguiente:
# 
# - Devolver el límite inferior si el número es menor que éste
# - Devolver el límite superior si el número es mayor que éste.
# - Devolver el número sin cambios si no se supera ningún límite.
# - Comprueba el resultado de recortar 15 entre los límites 0 y 10.

# In[13]:


def recortar (numero, minimo, maximo):
    if numero < minimo:
        print (minimo)
    elif numero > maximo: 
        print (maximo)
    else:
        print (numero)

recortar (12, 0, 10)


# Realiza una función separar(lista) que tome una lista de números enteros y devuelva dos listas ordenadas. La primera con los números pares y la segunda con los números impares.
# 
# 
# numeros = [-12, 84, 13, 20, -33, 101, 9]
# 

# In[18]:


numeros = [-12, 84, 13, 20, -33, 101, 9]

def separar(lista):
    lista.sort()
    pares = []
    impares = []
    for n in lista:
        if n%2 == 0:
            pares.append(n)
        else:
            impares.append(n)
    return pares, impares

pares, impares = separar(numeros)
print(pares)
print(impares)

