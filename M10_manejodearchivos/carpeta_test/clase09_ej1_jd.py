import sys

if len(sys.argv) == 4:
    p1 = sys.argv[1]
    p2 = sys.argv[2]
    p3 = sys.argv[3]
    print("Los parámetros ingresados son: |", p1, "|", p2, "|", p3)
else:
    print("Error - El número correcto de parámetros a ingresar es tres")
