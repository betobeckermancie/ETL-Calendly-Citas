import pandas as pd

file_path ="/dbfs/mnt/GoogleSheets/CSV's_Descargados/CitasCombinadas_Rename.csv"

#try: 
df=pd.read_csv(file_path)

#contar palabras de columna especifica
count_values = df['fraccionamiento'].value_counts()

#mostrar los resultados
print("Conteo de valores en la columna 'medio':")
print(count_values)

#Opcional: Guardar el conteo en un archivo csv
count_values.to_csv("/dbfs/mnt/GoogleSheets/CSV's_Descargados/Conteo_Medio.csv", header=["Conteo"])
print("Conteo guardado en: /dbfs/mnt/GoogleSheets/CSV's_Descargados/Conteo_Asesor.csv")

#except Exception as e:print(f"Error al procesar el archivo:{e}")

print("Proceso completado")