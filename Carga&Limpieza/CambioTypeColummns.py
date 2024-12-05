import pandas as pd
import os

#ruta donde estan los csvs
folder_path = "/dbfs/mnt/GoogleSheets/CSV's_descargados/"

#Iterar sobre los archivos de la carpeta
for file in os.listdir(folder_path):
    if file.endswith(".csv"): # verifica que sea un archivo csv
        file_path = os.path.join(folder_path, file)

        #leer el archivo csv
        df = pd.read_csv(file_path)

        #convertir columnas a los tipos de datos deseados
        df['cliente'] = df["cliente"].astype(str)
        df['medio']=df["medio"].astype(str)
        df['anuncio'] = df["anuncio"]. astype(str)
        df['fecha_cita'] = pd.to_datetime(df["fecha_cita"], format='%d/%m/%Y', errors='coerce')#convertir a fecha
        df['hora_cita'] = pd.to_datetime(df['hora_cita'], format='%H:%M', errors='coerce').dt.time()#REVISAR SI EL PARENTISIS NO CAUSA ERROR
        df["fraccionamiento"] = df["fraccionamiento"].astype(str)
        df["asesor"] = df["asesor"].astype(str)
        df["contacto_cliente"] = df["contacto_cliente"].astype(str) #mantener como texto para evitar problemas

        # Sobreescribir el archivo original con el dataframe formateado
        df.to_csv(file_path, index=False)
        print(f"Archivo formateado y sobreescrito: {file_path}")

    print("Proceso de cambio de tipos realizado.")
    


