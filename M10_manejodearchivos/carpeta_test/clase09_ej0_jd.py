def recibe():
    l_recibe = []
    nombre = input("Ingrese su nombre: ")
    l_recibe.append(nombre)
    edad = int(input("Ingrese su edad: "))
    l_recibe.append(edad)
    origen = input ("Indique su nacionalidad: ")
    l_recibe.append(origen)
    print(l_recibe)
recibe()