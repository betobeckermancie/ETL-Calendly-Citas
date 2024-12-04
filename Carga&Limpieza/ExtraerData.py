import gspread
from google.oauth2.service_account import Credentials
import pandas as pd
import os

#configuracion de credenciales
scopes =[
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

# Ruta al archivo de credenciales JSON en DBFS
json_creds_path = "/dbfs/mnt/GoogleSheets/Credenciales/GoogleSheets_Credenciales.json"

#cargar las credenciales con alcance definido
creds = Credentials.from_service_account(json_creds_path, scopes=scopes)
client = gspread.authorize(creds)

#Introducir el id del google sheet
sheet_id = "1ba6l4dFTroMgKk-zqI-jMBSEY4ZMgDJe7m3JrrtKXLE"# Aquí debes colocar el ID de tu hoja, ejemplo: "1dBFzUMXbEMDSPuoyDOi6L2gGnD-fnK1dNt4h8ei_H0"

#ruta base donde se guardaran los archivos csv
base_path   = "/dbfs/mnt/GoogleSheets/CSV's_Descargados/"

#crear el directorio si no existe
if not os.path.exists(base_path):
    os.makedirs(base_path)
    print(f"Directorio creado: {base_path}")
else:
    print(f"Directorio ya existente: {base_path}")

#conexion al google sheet por id
try:
    spreadsheet = client.open_by_key(sheet_id)
    print(f"Conexion exitosa al documento: {spreadsheet.title}")

    #descargar todas las hojas (wokrsheets) existentes
    worksheets = spreadsheet.worksheets()
    print("Hojas de calculo disponibles")
    for sheet in worksheets:
        print(f"- {sheet.title}")
        #descargar todos los registros de la hoja
        data= sheet.get_all_records() #descargar los datos como una lista de diccionarios
        df = pd.DataFrame(data) #convertir los datos a un dataframe de pandas
        print(f"\nDatos de la hoja '{sheet.title}':")
        print(df.head()) #mostrar las primeras filas para confirmar

        #Guardar cad a hoja como archivo csv en dbfs
        file_path = os.path.join(base_path, f"{sheet.title}.csv")
        df.to_csv(file_path, index=False)
        print(f"Datos de la hoja '{sheet.title}' guardados en: {file_path}")

except Exception as e:
    print(f"Error al conectar o procesar las hojas de calculo: {e}")



