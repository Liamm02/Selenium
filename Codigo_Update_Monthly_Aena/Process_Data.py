import pandas as pd
from datetime import datetime
from Constants import *
import warnings
from sqlalchemy.sql.elements import quoted_name

def Process_Data():
    try:
        month = Months[datetime.now().month - Consultar_Meses_Anteriores - 1]
        Year = datetime.now().year
        pd.set_option('display.max_columns', None)

        with warnings.catch_warnings(record=True):
            warnings.simplefilter("always")
            df = pd.read_excel(File_Path+Downloaded_File_Name, index_col=None, header=None,
                               names=["Compañía", "AeropuertoBase", "Año", "Mes", "Movimiento", "País", "PasajerosTotales"], skiprows=4)
            df.dropna(axis=1, how='all', inplace=True)
            # df = pd.read_excel(File_Path + Downloaded_File_Name, index_col=None, skiprows=2)

        if df.shape[1] != 7:
            print("Hubo algún problema en la descarga de los datos, el documento no cuenta con las columnas requeridas, volviendo a descargarlo...")
            return df, File_Path+Downloaded_File_Name, 1
        df["Compañía"].fillna(method='ffill', inplace=True)
        df["AeropuertoBase"].fillna(method='ffill', inplace=True)
        df["Mes"].fillna(method='ffill', inplace=True)
        df["Año"].fillna(method='ffill', inplace=True)

        df = df[df["Movimiento"] == "LLEGADA"]
        df['Año'] = df['Año'].astype(int)
        df = df[df["Año"] == Year]
        df = df.loc[df["AeropuertoBase"].isin(Aeropuertos), :]

        df["Mes"] = df["Mes"].str.split().str.get(0)
        df.set_index("Año", inplace=True)
        df = df[df["Mes"] == month]

        df = df[['AeropuertoBase', "Compañía", 'País', 'Mes', 'PasajerosTotales']]
        df.sort_values(['AeropuertoBase', 'País'],
                       ascending=[True, True], inplace=True)


        return df, Csv_path + "Aena_%s_%s.csv" % (Year, month), 0
    except FileNotFoundError:
        print("El archivo no se encuentra en la carpeta definida, reintentando la descarga...")
        return 0, Csv_path + "Aena_%s_%s.csv" % (Year, month), 1
