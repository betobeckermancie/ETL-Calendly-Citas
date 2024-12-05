import pandas as pd

#ruta al archivo csv especifico
file_path = "/dbfs/mnt/GoogleSheets/CSV's_Descargados/Combined_Data.csv"

#leer el archivo csv try 
try:
    df = pd.read_csv(file_path)

    #convertir valores de columnas declaradas a minusculas
    df['medio'] =df['medio'].str.lower()
    df['asesor']=df['asesor'].str.lower()
    df['fraccionamiento'] = df['fraccionamiento'].str.lower()

    #Sobre escribir el archivo original con los cambios
    df.to_csv(file_path, index=False)
    print(f"Valores de las columns 'medio' y 'asesor' convertidos a minusculas y guardados en: {file_path}")

except Exception as e:
    print(f"Error al procesar el archivo: {e}")

print("Cambio completado de contenido en columnas a minusculas.")

