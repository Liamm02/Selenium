import snowflake.connector
from snowflake.connector.pandas_tools import pd_writer
from snowflake.sqlalchemy import URL
from sqlalchemy import create_engine
from sqlalchemy.sql.elements import quoted_name
from Constants import *

def write_resultados_snowflake(final_df, fecha, file_error):
    try:
        # Escritura de tablas Metadatos y Clusters
        engine = create_engine(URL(
            user="DATA_SCIENTIST",
            password="FX0nCgiGg2ErhS7FCaPQkU1GeF7nAenIDsFNo4W1aYfpAloaEvphIkQj21PPrSme",
            account="satocan.eu-west-1",
            warehouse="DSML_WH",
            database="DEV_TURISMO",
            schema="RAW_AENA")
        )

        connection = engine.connect()

        # if_exists{‘fail’, ‘replace’, ‘append’}, default ‘fail’
        print("Lanzando sql para cargar PasajerosMesAnterior")
        final_df.to_sql(quoted_name('PasajerosMesAnterior', True), con=engine, if_exists='replace', index=False, method=pd_writer)

        connection.close()
        engine.dispose()
        print("Conexión a Snowflake cerrada.\t" + str(fecha))

    except Exception as e:
        f = open(file_error, 'w')
        f.write(Date_and_Hour + ': Error en escritura de resultados en Snowflake\nScript: Pasajeros Mes Anterior')
        print('Error: Escritura de resultados en Snowflake')
        print(e)
        f.close()
        return None