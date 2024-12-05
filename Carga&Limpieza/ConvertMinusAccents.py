#Codigo para cambio de columnas a minusculas y sin acentos
import unicodedata

#Ruta donde estan los csvs
folder_path = "/dbfs/mnt/GoogleSheets/CSV's_Descargados/"

#funcion para eliminar acentos de los nombres de las columnas
def remove_accents(column_name):
    return ''.join(
        char for char in unicodedata.normalize('NFD', column_name)
        if unicodedata.category(char) != 'Mn'
    )

#Iterar sobre los archivos de la carpeta 
for file in os.listdir(folder_path):
    if file.endswith(".csv"):# verifica que sea un archivo csv
        file_path = os.path.join(folder_path, file)

        # leer el archivo csv
        df = pd.read_csv(file_path, file)

        #convertir las columnas a minusculas y eliminar acentos
        df.columns = [remove_accents(col.lower()) for col in df.columns]

        #Sobre escribir el archivo original con el dataframe modificado
        df.to_csv(file_path, index=False)
        print(f"Archivo actualizado: {file_path}")

print("Proceso completado: columnas en minusculas y sin acentos.")

