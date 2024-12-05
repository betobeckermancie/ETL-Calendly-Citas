import pandas as pd

# Ruta al archivo CSV específico
file_path = "/dbfs/mnt/GoogleSheets/CSV's_Descargados/Combined_Data.csv"

# Leer el archivo CSV
try:
    df = pd.read_csv(file_path)

    # Reemplazar los valores que contengan 'crisina' o 'cristi' con 'cristina' en la columna 'asesor'
    df['asesor'] = df['asesor'].str.replace(r'\b(crisina|cristi)\b', 'cristina', case=False, regex=True)

    # Sobrescribir el archivo original con los cambios
    df.to_csv(file_path, index=False)
    print(f"Valores actualizados en la columna 'asesor' y guardados en: {file_path}")
    print("Proceso de reemplazo completado.")

except Exception as e:
    print(f"Error al procesar el archivo: {e}")
