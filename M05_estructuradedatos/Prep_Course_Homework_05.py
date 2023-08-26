#!/usr/bin/env python
# coding: utf-8

# ## Estructuras de Datos

# 1) Crear una lista que contenga nombres de ciudades del mundo que contenga más de 5 elementos e imprimir por pantalla

# In[3]:
ciudades = ["Londres", "Miami", "Bogotá", "Bombay", "Sidney", "Madrid", "Moscú"]
print (ciudades)



# 2) Imprimir por pantalla el segundo elemento de la lista

# In[4]:
print(ciudades[1])



# 3) Imprimir por pantalla del segundo al cuarto elemento

# In[8]:
print(ciudades[1:4])




# 4) Visualizar el tipo de dato de la lista

# In[12]:
print(type(ciudades))




# 5) Visualizar todos los elementos de la lista a partir del tercero de manera genérica, es decir, sin explicitar la posición del último elemento

# In[14]:
print(ciudades[2:])




# 6) Visualizar los primeros 4 elementos de la lista

# In[15]:
print(ciudades[0:4])


    


# 7) Agregar una ciudad más a la lista que ya exista y otra que no ¿Arroja algún tipo de error?

# In[16]:
ciudades.append("Dallas")
ciudades.append("Bogotá")
print(ciudades)








# 8) Agregar otra ciudad, pero en la cuarta posición

# In[20]:
ciudades.insert(3, "Medellín")
print(ciudades)




# In[21]:




# 9) Concatenar otra lista a la ya creada

# In[22]:
paises = ["Brasil", "Grecia", "Suiza"]
ciudades.extend(paises)
print(ciudades)



# 10) Encontrar el índice de la ciudad que en el punto 7 agregamos duplicada. ¿Se nota alguna particularidad?

# In[23]:
print(ciudades.index("Bogotá")) # Solo lista la primera coincidencia




# 11) ¿Qué pasa si se busca un elemento que no existe?

# In[24]:
# print(ciudades.index("Méjico")) # Python devuelve ValueError




# 12) Eliminar un elemento de la lista

# In[25]:
ciudades.remove("Moscú")
print(ciudades)




# 13) ¿Qué pasa si el elemento a eliminar no existe?

# In[27]:
# ciudades.remove("Quito") # Python devuelve ValueError




# 14) Extraer el úlimo elemento de la lista, guardarlo en una variable e imprimirlo

# In[28]:
ult_ciudades = ciudades.pop()
print(ult_ciudades)




# 15) Mostrar la lista multiplicada por 4

# In[29]:
multp4 = ciudades * 4
print (multp4)



# 16) Crear una tupla que contenga los números enteros del 1 al 20

# In[32]:
l1 = []
for i in range (1,21):
    l1.append(i)
tp_l1 = tuple(l1)
print(tp_l1)



# 17) Imprimir desde el índice 10 al 15 de la tupla

# In[35]:
print(tp_l1[10:16])



# 18) Evaluar si los números 20 y 30 están dentro de la tupla

# In[41]:
for i1 in (tp_l1):
    if i1 == 20:
        print("El 20 hace parte de la tupla")
    elif i1 == 30:
        print("El 30 hace parte de la tupla")
    else:
        continue




# 19) Con la lista creada en el punto 1, validar la existencia del elemento 'París' y si no existe, agregarlo. Utilizar una variable e informar lo sucedido.

# In[48]:
ciudades1 = ["Londres", "Miami", "Bogotá", "Bombay", "París", "Sidney", "Madrid", "Moscú"]
x = 0
for i in ciudades1:
    if i == "París":
        x = 1
        (print("Ya existe París"))
        break
if x == 0:
    ciudades1.append("París")
    (print("París ha sido agregada"))
print(ciudades1)




# 20) Mostrar la cantidad de veces que se encuentra un elemento específico dentro de la tupla y de la lista

# In[51]:
print(tp_l1.count(20))
print(ciudades1.count("Bogotá"))




# 21) Convertir la tupla en una lista

# In[52]:
t21 = (3,67,34,89,0,23)
l_t21 = list(t21)
print(l_t21)
print(type(l_t21))




# 22) Desempaquetar solo los primeros 3 elementos de la tupla en 3 variables

# In[55]:
a, b, c, _, _, _ = t21
print (a)
print (b)
print (c)




# 23) Crear un diccionario utilizando la lista crada en el punto 1, asignandole la clave "ciudad". Agregar tambien otras claves, como puede ser "Pais" y "Continente".

# In[57]:
ciudades = ["Londres", "Miami", "Bogotá", "Bombay", "Sidney", "Madrid", "Moscú"]
paises = ["India", "Inglaterra", "Argentina", "Lituania", "España", "Rusia", "Colombia"]
continentes = ["América", "África", "Europa", "Oceanía"]
dic_geo = {"ciudad" : ciudades, "pais" : paises, "continente" : continentes}
print(dic_geo)





# 24) Imprimir las claves del diccionario

# In[59]:
print(dic_geo.keys())



# 25) Imprimir las ciudades a través de su clave

# In[61]:
for i,j in list(dic_geo.items()):
    if i == "ciudad":
        print(j)



