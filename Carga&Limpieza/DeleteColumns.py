import pandas as pd
import os

#ruta donde estan los csvs
folder_path ="/dbfs/mnt/GoogleSheets/CSV's_Descargados/"

#Iterar sobre los archivos en la carpeta
for file in os.listdir(folder_path):
    if file.endswith(".csv"): #verifica que sea un archivo csv
        file_path = os.path.join(folder_path,file)

        # leer el archivo csv
        df = pd.read_csv(file_path)

        #filtrar las columnas eliminando las que se llamen 'Unnamed','landings' o 'Dia'
        columns_to_remove = [col for col in df.columns if "Unnamed" in col or col in ["landings","Día","dia"]]
        df = df.drop(columns= columns_to_remove, errors="ignore")

        #sobreescribir el archivo original con el dataframe limpio
        df.to_csv(file_path, index=False)
        print(f"Archivo limpiado y sobreescrito_ {file_path}")

    print("Proceso de limpieza completado")

    
