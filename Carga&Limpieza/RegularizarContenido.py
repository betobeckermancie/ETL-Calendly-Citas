#Regularizacion de variables en columnas para facilitar el analisis (para informacion escrita de muchas formas con el mismo significado)

import pandas as pd

#Ruta al archivo csv especifico
file_path = "/dbfs/mnt/GoogleSheets/CSV's_Descargados/Combined_Data.csv"

#leer el archivo csv
try:
    df= pd.read_csv(file_path)

    #remplazar valores especificos en la columna 'medio'
    replacements = {
        r'\bface\b': 'facebook', #cambiar 'face' por 'facebook'
        r'\bpag\s*web\b': 'pagina web', #cambiar 'pag web' por 'pagina web'
        r'\bwhats\b': 'whatsapp' #cambiar 'whats' por 'whatsapp'
    }

    for pattern, replacement in replacements.items():
        df['medio'] = df['medio'].str.replace(pattern, replacement, case=False, regex=True)

    # sobreescribir el archivo original con los cambios
    df.to_csv(file_path,index=False)
    print(f"Valores actualizados en la columna 'medio' y guardados en: {file_path}")

    print("Proceso de remplazo con normalizacion completado.")

except Exception as e:
    print(f"Error al procesar el archivo: {e}")