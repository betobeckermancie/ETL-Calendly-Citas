#codigo para renombrar columnas de todos los archivos

import pandas as pd
import os

#ruta domde estam los csvs
folder_path = "/dbfs/mnt/GoogleSheets/CSV's_Descargados/"

# iterar sobre los archivos en la carpeta
for file in os.listdir(folder_path):
    if file.endswith(".csv"): #Verifica que sea un archivo csv
        file_path = os.path.join(folder_path, file)

        #leer el archivo csv
        df = pd.read_csv(file_path)

        #renombar columnas segun el mapeo
        df.rename(columns={
            "nombre": "cliente",
            "ad": "anuncio",
            "fecha": "fecha_cita",
            "hora": "hora_cita",
            "telefono": "contacto_cliente",
            }, inplace=True)
        
        #Guardar el archivo actualizado en el mismo lugar
        df.to_csv(file_path, index=False)
        print(f"Archivo procesado y guardado: {file_path}")

print("Renombrado de columnas completado.")

