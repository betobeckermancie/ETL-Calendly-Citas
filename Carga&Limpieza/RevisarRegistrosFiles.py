#contamos cuantos registros tienen los archivos que existen dentro de una ruta

import os
import pandas as pd

#Ruta de la carpeta donde estan los archivos
folder_path = "/dbfs/mnt/GoogleSheets/CSV's_Descargados/"

#inicializar contadores
total_records =0
file_records= {}

#recorrer todos los archivos en la carpeta
for file_name in os.listdir(folder_path):
    file_path = os.path.join(folder_path,file_name)

    #verificar si es un archivo (y o una capeta)
    if os.path.isfile(file_path):
        try:
            #Procesar solo archivos csv o txt(agregar mas formatos si es necesario)
            if file_name.endswith(".csv"):
                #Leer el archivo csv
                df = pd.read_csv(file_path)
                records = len(df)
                file_records[file_name]= records
                total_records += records
            elif file_name.endswith(".txt"):
                #leer archivo de texto linea por linea
                with open(file_path, "r") as f:
                    records = sum(1 for line in f)
                file_records[file_name]= records
                total_records += records
        except Exception as e:
            print(f"Error procesando el archivo {file_name}: {e}")

#Mostrar los resultados
print("Cantidad de registros por archivo:")
for file, count in file_records.items():
    print(f"{file}: {count} registros")

print(f"\nCantidad total de registros en la carpeta: {total_records}")