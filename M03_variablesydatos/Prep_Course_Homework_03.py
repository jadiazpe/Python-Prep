#!/usr/bin/env python
# coding: utf-8

# ## Variables

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantallaç

# In[7]:
n_entero = 10
print (n_entero)



# 2) Imprimir el tipo de dato de la constante 8.5

# In[3]:
print(type(8.5))




# 3) Imprimir el tipo de dato de la variable creada en el punto 1

# In[8]:
print(type(n_entero))




# 4) Crear una variable que contenga tu nombre

# In[2]:
nombre = 'Jairo'
nombre



# 5) Crear una variable que contenga un número complejo

# In[3]:
complejo = 2+8j
complejo




# 6) Mostrar el tipo de dato de la variable crada en el punto 5

# In[4]:
print(type(complejo))




# 7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales

# In[1]:
n_pi = 3.1416
print(n_pi)


# 8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?

# In[3]:
verdad = 'True' # String
status_verdad = True # Boolean




# 9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 8

# In[5]:
print(type(verdad))
print(type(status_verdad))




# 10) Asignar a una variable, la suma de un número entero y otro decimal

# In[1]:
ent_dec = 7 + 3.2
print(ent_dec)




# 11) Realizar una operación de suma de números complejos

# In[2]:
sum_complejos = (2+8j) + (8+1j)
print (sum_complejos)




# 12) Realizar una operación de suma de un número real y otro complejo

# In[4]:
real_complejo = 6.7 + (4+6j)
print(real_complejo)




# 13) Realizar una operación de multiplicación

# In[5]:
mult_real_complejo = (10.7+6j) * 5
print (mult_real_complejo)




# 14) Mostrar el resultado de elevar 2 a la octava potencia

# In[6]:
pot = 2**8
print (pot)



# 15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla

# In[8]:
cociente15 = 27 / 4
print(cociente15)




# 16) De la división anterior solamente mostrar la parte entera

# In[9]:
cociente16 = 27 // 4
print(cociente16)




# 17) De la división de 27 entre 4 mostrar solamente el resto

# In[1]:
cociente17 = 27 % 4
print(cociente17)




# 18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado

# In[2]:
qn27 = ((cociente16) * 4) + cociente17
print(qn27)




# 19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas

# In[3]:
x = 'jairo:53 '
y = 'fefo:23 '
z = 'cami:22 '
print ("edades", x + y + z)




# 20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?

# In[4]:
# "2" = 2 --> Error evaluating with "=" / since "=" is an assignation operator
"2" == 2 # Return False / "2" is a string - 2 is an integer




# 21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera

# In[11]:
2 == int("2")




# 22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')

# In[12]:
# a = float('3,8') Error: expected "." instead of ","




# 23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido y que de como resultado 2.

# In[15]:
n_dec = 3
n_dec -= 1
print(n_dec)



# 24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?

# In[29]:
1 << 2 # Moves the first binary number position two places, from right to left ... filling with zeros to the right. That chances the decimal number from 1 to 4 
 



# 25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?

# In[23]:
# 2 + '2' Can´t operate int and str using "+"  
sum_alpha = 2 + int('2')
print(sum_alpha)
add_alpha = str(2) + '2'
print(add_alpha)



# 26) Realizar una operación válida entre valores de tipo entero y string

# In[30]:
l = 'jairo ' * 3
print(l)


