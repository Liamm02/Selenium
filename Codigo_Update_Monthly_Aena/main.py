from datetime import datetime

from Download_Document import Download_Document
from Process_Data import Process_Data
from Delete_Old_Document import Delete_Old_Document
from Constants import *
from Write_Resultados_Snowflake import write_resultados_snowflake
from Validate_Snowflake import validate
import time


Proper_Execution = 1
Delete_Old_Document("./ErrorLogs.txt")
while Proper_Execution == 1:
    Delete_Old_Document(File_Path + Downloaded_File_Name)
    Proper_Execution = Download_Document()
    time.sleep(3)
    if Proper_Execution == 0:
        df, New_Document_Path, Proper_Execution = Process_Data()


if df.empty == False:

    print("Month uploaded to Aena, updating Snowflake Raw")
    write_resultados_snowflake(df,datetime.now().replace(microsecond=0),"./ErrorLogs.txt")
    print("Datos actualizados")
else:
    print("La información para este mes no ha sido actualizada aún")







