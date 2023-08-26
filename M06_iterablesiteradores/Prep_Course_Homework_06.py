#!/usr/bin/env python
# coding: utf-8

# ## Iteradores e iterables

# 1) A partir de una lista vacía, utilizar un ciclo while para cargar allí números negativos del -15 al -1

# In[1]:
lst1 = []
cont1 = -15
while cont1 <= -1:
    lst1.append(cont1)
    cont1 += 1
print(lst1)




# 2) ¿Con un ciclo while sería posible recorrer la lista para imprimir sólo los números pares?

# In[3]:
cont1 = -15
while cont1 <= -1:
    if cont1 % 2 == 0:
        print(cont1, end=" ")
    cont1 += 1




# 3) Resolver el punto anterior sin utilizar un ciclo while

# In[4]:
for i in (lst1):
    if i%2 == 0:
        print(i, end=" ")
#[i for i in lst1 if i%2 == 0] # Using list comprehension




# 4) Utilizar el iterable para recorrer sólo los primeros 3 elementos

# In[7]:
for i in (lst1[0:3]):
    print(i, end=" ")



# 5) Utilizar la función **enumerate** para obtener dentro del iterable, tambien el índice al que corresponde el elemento

# In[9]:
for idx, ele in enumerate(lst1):
    print(idx, ele)



# 6) Dada la siguiente lista de números enteros entre 1 y 20, crear un ciclo donde se completen los valores faltantes: lista = [1,2,5,7,8,10,13,14,15,17,20]

# In[10]:
lista = [1,2,5,7,8,10,13,14,15,17,20]
cont3 = 0
for i in lista:
    cont3 += 1
    if cont3 == i:
        continue
    else:
        lista.insert((cont3-1), cont3)
print(lista)




# In[11]:


n = 1



# 7) La sucesión de Fibonacci es un listado de números que sigue la fórmula: <br>
# n<sub>0</sub> = 0<br>
# n<sub>1</sub> = 1<br>
# n<sub>i</sub> = n<sub>i-1</sub> + n<sub>i-2</sub><br>
# Crear una lista con los primeros treinta números de la sucesión.<br>

# In[23]:
fib = []
fib.extend([0 ,1])
n = 2
while n < 30:
    fib.append(fib[n-1]+fib[n-2])
    n += 1
print(fib)    




# 8) Realizar la suma de todos elementos de la lista del punto anterior

# In[24]:
print(sum(fib))



# 9) La proporción aurea se expresa con una proporción matemática que nace el número irracional Phi= 1,618… que los griegos llamaron número áureo. El cuál se puede aproximar con la sucesión de Fibonacci. Con la lista del ejercicio anterior, imprimir el cociente de los últimos 5 pares de dos números contiguos:<br>
# Donde i es la cantidad total de elementos<br>
# n<sub>i-1</sub> / n<sub>i</sub><br>
# n<sub>i-2</sub> / n<sub>i-1</sub><br>
# n<sub>i-3</sub> / n<sub>i-2</sub><br>
# n<sub>i-4</sub> / n<sub>i-3</sub><br>
# n<sub>i-5</sub> / n<sub>i-4</sub><br>
#  

# In[38]:
n = 25
while n < 30:
    print(fib[n]/fib[n-1])
    n += 1



# 10) A partir de la variable cadena ya dada, mostrar en qué posiciones aparece la letra "n"<br>
# cadena = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'

# In[39]:
cadena = 'Hola Mundo. Esto es una práctica del lenguaje de programación Python'
for i,c in enumerate(cadena):
        if c == "n":
            print("letra 'n' en la posición: ", i)




# 11) Crear un diccionario e imprimir sus claves utilizando un iterador

# In[40]:
alfa = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9}
for i,j in alfa.items():
    print(i)




# 12) Convertir en una lista la variable "cadena" del punto 10 y luego recorrerla con un iterador 

# In[41]:





# In[45]:
lst_cadena = list(cadena)
print(lst_cadena)
for i in lst_cadena:
    print(i,"/", end=" ")




# 13) Crear dos listas y unirlas en una tupla utilizando la función zip

# In[48]:
lista13 = [1,2,5,7,8,10,13,14,15,17,20]
lista131 = ["Colombia", "Perú", "Argentina", "Bolivia", "Pánama"]
lista132 = zip(lista13, lista131)
print(lista132)
print(type(lista132))
print(list(lista132))




# 14) A partir de la siguiente lista de números, crear una nueva sólo si el número es divisible por 7<br>
# lis = [18,21,29,32,35,42,56,60,63,71,84,90,91,100]

# In[49]:
lis = [18,21,29,32,35,42,56,60,63,71,84,90,91,100]
lis7 = [i for i in lis if i%7 == 0]
print(lis7)




# 15) A partir de la lista de a continuación, contar la cantidad total de elementos que contiene, teniendo en cuenta que un elemento de la lista podría ser otra lista:<br>
# lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]

# In[56]:
lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]
lis_contar = []
for i in lis:
    if type(i) == list:
        lis_contar.extend(i)
    else:
        lis_contar.append(i)
print("El número de elementos de 'lis' es :", len(lis_contar))



# In[51]:





# In[57]:





# 16) Tomar la lista del punto anterior y convertir cada elemento en una lista si no lo es

# In[58]:
lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]
for i,j in enumerate(lis):
    if type(j) == list:
        continue
    else:
        lis[i] = [j]   
print(lis)


