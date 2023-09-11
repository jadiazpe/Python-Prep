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