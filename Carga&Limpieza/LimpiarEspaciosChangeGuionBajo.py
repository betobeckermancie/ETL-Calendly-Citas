### quitar espacios en blanco y cambiarlos por '_' guiones bajos dentro del contenido
# de las columnas indicadas

import pandas as pd

#Ruta del archivo especifico
file_path = "/dbfs/mnt/GoogleSheets/CSV's_Descargados/Combined_Data.csv"

#leer el archivo csv
df = pd.read_csv(file_path)

#lista de columnas a procesar
columns_to_process = ["cliente", "medio", "anuncio","fraccionamiento", "asesor"]

#limiar y remplanzar espacios entre las palabras dentro de las columnas por guiones
#bajos
for column in columns_to_process:
    df[column] = df[column].apply(lambda x: '_'.join(x.strip()) if isinstance(x, str) else x)

#Guardar los cambios sobreescribiendo el archivo original
df.to_csv(file_path, index=False)

#imprimir resultado
print(f"Archivo actualizado con espacios limpiados y remplazados por guiones bajos: {file_path}")

