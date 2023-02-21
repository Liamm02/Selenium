import getpass
from datetime import datetime

Months = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre",
          "Noviembre", "Diciembre"]
Aeropuertos = ["FUERTEVENTURA", "GRAN CANARIA", "LANZAROTE CÉSAR MANRIQUE", "TENERIFE NORTE-C. LA LAGUNA",
               "TENERIFE SUR"]
AENA = "https://www.aena.es/es/estadisticas/consultas-personalizadas.html"
Downloaded_File_Name = "Pasajeros por Compañía.xlsx"
File_Path = "C:/Users/%s/Downloads/" % (getpass.getuser())
Csv_path = "C:/Users/%s/Downloads/" % (getpass.getuser())
Satocan_Aena_Folder_ID = '1OyqPKB0_exn6sFU6COvM7coC7bZ1qeuS'
# Sumar 1 a Consultar_Mes_Anterior por cada mes hacia atrás que queramos consultar. Mes actual = 0, Mes anterior = 1
# No debe usarse para procesar meses de año
Consultar_Meses_Anteriores = 1
Date_and_Hour = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
