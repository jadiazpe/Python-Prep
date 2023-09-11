import sys
import os
import csv
import datetime

if len(sys.argv) == 4:
    t = []
    h = ["Timestamp", "Celsius", "Humedad", "Lluvia"]
    dt = datetime.datetime.now()
    ts = datetime.datetime.timestamp(dt)

    t.append(ts)
    celsius = sys.argv[1]
    t.append(celsius)
    humedad = sys.argv[2]
    t.append(humedad)
    lluvia = sys.argv[3]
    t.append(lluvia)
    print("Los parámetros ingresados son: |", celsius, "|", humedad, "|", lluvia)
    print(t)
    if os.path.exists("C:\DATA_SCIENCE\PREP_REPOSITORY\Python-Prep\M10_manejodearchivos\carpeta_test\clase09_ej2_jd.csv"):
        print("El archivo existe")
        with open("C:\DATA_SCIENCE\PREP_REPOSITORY\Python-Prep\M10_manejodearchivos\carpeta_test\clase09_ej2_jd.csv", "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(t)    
    else:
        with open("C:\DATA_SCIENCE\PREP_REPOSITORY\Python-Prep\M10_manejodearchivos\carpeta_test\clase09_ej2_jd.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(h)
            writer.writerow(t)        
else:
    print("Error - El número correcto de parámetros a ingresar es tres")



