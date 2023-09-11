# 1. MODULES
import sys
import os
import csv

# 2. ENTRIES
cont = 0
headers = []
datos = []
montañas = {'nombre':[  'Everest','K2','Kanchenjunga','Lhotse','Makalu',
                        'Cho Oyu','Dhaulagiri','Manaslu','Nanga Parbat','Annapurna I'],
            'orden':[1,2,3,4,5,6,7,8,9,10],
            'cordillera':['Himalaya','Karakórum','Himalaya','Himalaya','Himalaya'
                        ,'Himalaya','Himalaya','Himalaya','Karakórum','Himalaya'],
            'pais': ['Nepal','Pakistán','Nepal','Nepal','Nepal','Nepal','Nepal','Nepal',
                    'Pakistán','Nepal'],
            'altura':[8849,8611,8586,8516,8485,8188,8167,8163,8125,8091]}

#############################################################################################
# 3. PROCESS
for i,j in montañas.items():
    headers.append(i)
    datos.append(j)

with open("C:\DATA_SCIENCE\PREP_REPOSITORY\Python-Prep\M10_manejodearchivos\carpeta_test\clase09_ej3_jd.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    while (cont < 10):
        f.write(montañas['nombre'][cont]+',')
        f.write(str(montañas['orden'][cont])+',') # Convierte número a string para permitir la copia
        f.write(montañas['cordillera'][cont]+',')
        f.write(montañas['pais'][cont]+',')
        f.write(str(montañas['altura'][cont])+'\n') # Convierte número a string para permitir la copia
        cont += 1    
            



            