import pandas as pd
import os

#Ruta donde estan los csvs
folder_path = "/dbfs/mnt/GoogleSheets/CSV's_Descargados/"

#Lisa para almacenar los dataframes
dataframes = []

#Iterar sobre los archivos de la carpeta
for file in os.listdir(folder_path):
    if file.endswith(".csv"): #verifica que sea un archivo csv
        file_path = os.path.join(folder_path, file)

        #Leer el archivo csv
        df = pd.read_csv(file_path)

        #Agregar el DataFrame a la lista
        dataframes.append(df)

#Combinar los dataframes por columnas comunes
combined_df = pd.concat(dataframes, axis=0, join="inner", ignore_index=True)

#Guardar el dataframe combinado en un nuevo archivo
output_path = os.path.join(folder_path, "Combined_Data.csv")
combined_df.to_csv(output_path, index=False)

print(f"Se han combinado todos los archivos: {output_path}")

