#!/usr/bin/env python
# coding: utf-8

# ## Clases y Programación Orientada a Objetos

# 1) Crear la clase vehículo que contenga los atributos:<br>
# Color<br>
# Si es moto, auto, camioneta ó camión<br>
# Cilindrada del motor

# In[1]:
class Vehiculo:
    def __init__(self, color, tipo, cilindraje):
        self.color = color
        self.tipo = tipo
        self.cilindraje = cilindraje



# 2) A la clase Vehiculo creada en el punto 1, agregar los siguientes métodos:<br>
# Acelerar<br>
# Frenar<br>
# Doblar<br>

# In[5]:
class Vehiculo:
    def __init__(self, color, tipo, cilindraje):
        self.color = color
        self.tipo = tipo
        self.cilindraje = cilindraje
        self.acelera = 0
        self.gira = 0
    def estado_acelerar(self, acelera):
        self.acelera += acelera
    def estado_frenar(self, frena):
        self.frena -= frena
    def estado_girar(self, gira):
        self.gira += gira
    def descripcion_basica(self):
        return print("Vehículo tipo:", self.tipo, "|Color:", self.color, "|Cilindraje cc:", self.cilindraje)
    def describe_estado(self):
        return print("Velocidad km/hr:", self.acelera, "|Dirección en grados:", self.gira)




# 3) Instanciar 3 objetos de la clase vehículo y ejecutar sus métodos, probar luego el resultado

# In[6]:
a001 = Vehiculo("Negro", "Moto", 250)
a002 = Vehiculo("Rojo", "Moto", 500)
a030 = Vehiculo("Blanco", "Camioneta", 3000)
a020 = Vehiculo("VerdeClaro", "Auto", 1800)
a002.estado_acelerar(200)
a002.estado_girar(-30)
a002.estado_acelerar(100)
#a002.estado_frenar(60)
a001.estado_acelerar(240)
a001.estado_girar(57)




# 4) Agregar a la clase Vehiculo, un método que muestre su estado, es decir, a que velocidad se encuentra y su dirección. Y otro método que muestre color, tipo y cilindrada

# In[12]:
a002.descripcion_basica()
a002.describe_estado()





# In[13]:
a001.descripcion_basica()
a001.describe_estado()





# 5) Crear una clase que permita utilizar las funciones creadas en la práctica del módulo 7<br>
# Verificar Primo<br>
# Valor modal<br>
# Conversión grados<br>
# Factorial<br>

# In[33]:
class Operatividad:

    def __init__(self) -> None:
        pass
    
    def primo (x):
        si_primo = True
        if x == 2:
            return True
        for i in range (2, x):
            if x % i == 0:
                si_primo = False
                break
        return si_primo
    
    def ocurrencia(lst):
        lst_rep = dict()
        for i in lst:
            lst_rep[i] = lst.count(i)
            lst_rep_orden = sorted(lst_rep.items(), key=lambda item:item[1], reverse=True)
        for l,m in enumerate(lst_rep_orden):
            return "El número que más se repite es", m[0], "con", m[1], "ocurrencias"
        
    def temperatura(valor, ent_med, sal_med):
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
    
    def factorial(x):
        import numpy
        f = []
        if type(x) != int or x < 0 :
            return "Debe ingresar un número entero mayor que cero"
        else:
            for i in range(1,(x+1)):
                f.append(i)
                fac = numpy.prod(f)
        return fac





# 6) Probar las funciones incorporadas en la clase del punto 5

# In[28]:
print(type(Operatividad))
Operatividad.primo(101)
lst = [5,8,23,20,15]
Operatividad.ocurrencia(lst)
Operatividad.factorial(5)
Operatividad.temperatura(10,"Kelvin","Farenheit")



# 7) Es necesario que la clase creada en el punto 5 contenga una lista, sobre la cual se aplquen las funciones incorporadas

# In[55]:
class Operatividad:

    def __init__(self, listado):
        self.listado = listado

    def primo_listado(self):
        for i,j in enumerate(self.listado):
            if (self.primo(j)) == True:
                print("El número:", j, "que aparece en la lista en posición", i, ">>> ES PRIMO")
            elif (self.primo(j)) == None:
                print("El número:", j, "que aparece en la lista en posición", i, "es igual o menor que CERO")
            else:
                print("El número:", j, "que aparece en la lista en posición", i, ">>> NO es PRIMO") 
          
    def ocurrencia_listado(self):
        lst = self.listado
        print("El número más repetido en la lista es el primero de la tupla. El segundo número es su frecuencia:", self.ocurrencia(lst))

    def temperatura_listado(self, ent_med, sal_med):
        for i in (self.listado):
            print(i, "Grados", ent_med, "son equivalentes a", self.temperatura(i, ent_med, sal_med), "Grados", sal_med)

    def factorial_listado(self):
        for n in (self.listado):
            print ("El cálculo factorial para el número", n, "de la lista es igual a: ", self.factorial(n))
            
    #############################################################################################################################
    
    def primo(self, x):
        si_primo = True
        if x == 2:
            return True
        elif x == 1:
            return False
        elif x <= 0:
            return None
        for i in range (2, x):
            if x % i == 0:
                si_primo = False
                break
        return si_primo
    
    def ocurrencia(self, lst):
        lst_rep = dict()
        lst1 = []
        for i in lst:
            lst_rep[i] = lst.count(i)
            lst_rep_orden = sorted(lst_rep.items(), key=lambda item:item[1], reverse=True)
        lst1.extend(lst_rep_orden[0])
        return lst1[0], lst1[1]
        
    def temperatura(self, valor, ent_med, sal_med):
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
    
    def factorial(self, x):
        import numpy
        f = []
        if type(x) != int:
            return "Debe ingresar un número entero mayor que cero"
        elif x == 0:
            return 1
        elif x < 0:
            return None
        else:
            for i in range(1,(x+1)):
                f.append(i)
                fac = numpy.prod(f)
        return fac
    

opera = Operatividad([2,7,4,3,4,3,4,3,7,6,4,4,6,2,4,1,6,5,4,7,3,3,3,0,-4,-5,-1])
type(opera)
opera.primo_listado()
opera.ocurrencia_listado()
opera.factorial_listado()
opera.temperatura_listado("Farenheit", "Celsius")

# 8) Crear un archivo .py aparte y ubicar allí la clase generada en el punto anterior. Luego realizar la importación del módulo y probar alguna de sus funciones

# In[1]:
from operatividad import *
opera1 = Operatividad([2,7,4,3,4,3,4,3,7,6,4,4,6,2,4,1,6,5,4,7,3,3,3,0,-4,-5,-1])
opera1.factorial_listado()
opera1.temperatura_listado("Kelvin", "Farenheit")



