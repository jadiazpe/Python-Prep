#!/usr/bin/env python
# coding: utf-8

# ## Funciones

# 1) Crear una función que reciba un número como parámetro y devuelva si True si es primo y False si no lo es

# In[1]:
def primo(n):
    cont = 0
    divisores = []
    if n == 2:
        return True
    for i in range (2, n):
        divisores.append(i)
    for j in divisores:
        if n % j == 0:
            return False
        else:
            cont += 1
    if cont != 0:
        return True 
primo(102)




# 2) Utilizando la función del punto 1, realizar otra función que reciba de parámetro una lista de números y devuelva sólo aquellos que son primos en otra lista

# In[25]:
def lst_primos(x2):
    prim = True
    primos = []
    for i in (lpr):
        for j in range (2, i):
            if i % j == 0:
                prim = False
                break
        if prim == True:
            primos.append(i)
        else:
            prim = True
    return primos
lpr = [32,5,4,7,11,100,101,13,19,21,37]
lst_primos (lpr)



# 3) Crear una función que al recibir una lista de números, devuelva el que más se repite y cuántas veces lo hace. Si hay más de un "más repetido", que devuelva cualquiera

# In[33]:
def ocurrencia(x3):
    lst3_rep = dict()
    for i in lst3:
        lst3_rep[i] = lst3.count(i)
    lst3_rep_orden = sorted(lst3_rep.items(), key=lambda item:item[1], reverse=True)
    for l,m in enumerate(lst3_rep_orden):
            return "El número que más se repite es", m[0], "con", m[1], "ocurrencias"
lst3 = [5,7,11,3,4,3,67,34,7,67,4,3,67,11,67,4,4,67,32,4,16,5,4,67,3,3,3]
ocurrencia(lst3)




# 4) Crear una función que convierta entre grados Celsius, Farenheit y Kelvin<br>
# Fórmula 1	: (°C × 9/5) + 32 = °F<br>
# Fórmula 2	: °C + 273.15 = °K<br>
# Debe recibir 3 parámetros: el valor, la medida de orígen y la medida de destino
# 

# In[56]:
def temperatura2 (valor, ent_med, sal_med):
    if ent_med == "Celsius":
        if sal_med == "Farenheit":
            salida = (valor * (9 / 5) + 32)
        elif sal_med == "Kelvin":
            salida = (valor + 273.15)
    if ent_med == "Farenheit":
        if sal_med == "Celsius":
            salida = (valor - 32) / (9 / 5)
        elif sal_med == "Kelvin":
            salida = ((valor - 32) / (9 / 5)) + 273.15
    if ent_med == "Kelvin":
        if sal_med == "Celsius":
            salida = valor - 273.15
        elif sal_med == "Farenheit":
            salida = ((valor - 273.15) * (9 / 5)) + 32
    return round(salida,2)


# 5) Iterando una lista con los tres valores posibles de temperatura que recibe la función del punto 5, hacer un print para cada combinación de los mismos:

# In[62]:
escalas = ["Celsius","Farenheit","Kelvin"]
x = 10
print(">>> Valor de Entrada =", x, "Grados <<<")
for i in escalas:
    print("* Escala", i, ":")
    for j in range(0, 3):
        if i == escalas[j]:
            continue
        print(x, "Grados", i, "equivalen a", temperatura2(x, i, escalas[j]), "Grados", escalas[j])



# 6) Armar una función que devuelva el factorial de un número. Tener en cuenta que el usuario puede equivocarse y enviar de parámetro un número no entero o negativo

# In[65]:
def factor(x):
    if type(x) != int or x < 0 :
        return "Debe ingresar un número entero mayor que cero"
    else:
        fac = 1
        for i in range(1,(x+1)):
            fac = fac * i
    return fac
factor(4)



