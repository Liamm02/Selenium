from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import time
import pandas as pd
from datetime import datetime
import os

def Find_Years():
    options = Options()

    options.add_argument('--disable-extensions')
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get("https://www.aena.es/es/estadisticas/consultas-personalizadas.html")
    driver.set_window_size(1600, 768)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "button.ecix-bold ecix-font-1-2em elix-accordion-btn-primary elix-deny-all-hidden-2".replace(" " , ".")))).click()

    lnks=driver.find_elements(By.CLASS_NAME, "nav-link btn azul centrado".replace(" ", "."))
    lnks[3].click()

    time.sleep(5)
    # Cambiamos al IFrame
    WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.ID, 'EurolandTool')))
    # iframe = driver.find_element(By.ID, 'EurolandTool')
    # driver.switch_to.frame(iframe)

    divContenedor = driver.find_element(By.ID, 'id_mstr50')
    imagenes = divContenedor.find_elements(By.TAG_NAME, 'IMG')
    imagen = imagenes[0]
    print("Esperando respuesta de Aena")
    time.sleep(5)
    action = ActionChains(driver)
    action.move_by_offset(300, 450).double_click().perform()
    action.move_by_offset(-300, -450).perform()



    driver.switch_to.default_content()

    driver.execute_script("window.scrollTo(0, 600);")

    action.move_by_offset(225,480).click().perform()
    action.move_by_offset(-225,-480).perform()
    driver.execute_script("window.scrollTo(0, 150);")

    time.sleep(10)

    print("Filtrando información")
    #Aeropuerto base
    action.move_by_offset(300,275).double_click().perform()
    time.sleep(6)
    #Compañía
    action.move_by_offset(0, 90).double_click().perform()
    time.sleep(6)
    #Mes
    action.move_by_offset(0, 60).double_click().perform()
    time.sleep(4)
    #Movimiento
    action.move_by_offset(0, 20).double_click().perform()
    time.sleep(4)
    #Pais
    action.move_by_offset(0, 30).double_click().perform()
    time.sleep(4)

    #Descarga de archivo.
    action.move_by_offset(-300, -475).perform()
    action.move_by_offset(1360, 345).perform()
    action.click().perform()
    time.sleep(1)

    print("Descargando información")
    action.move_by_offset(0, 50).perform()
    action.click().perform()
    time.sleep(1)
    action.move_by_offset(-150, 5).perform()
    action.click().perform()





#$0.getBoundingClientRect()




# Find_Years()

path = "C:/Users/lmahmud/Downloads/Pasajeros por Compañía.xlsx"
Months = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre" ,"Noviembre", "Diciembre"]
Aeropuertos = ["FUERTEVENTURA", "GRAN CANARIA", "LANZAROTE CÉSAR MANRIQUE", "TENERIFE NORTE-C. LA LAGUNA", "TENERIFE SUR"]
month = Months[datetime.now().month-2]
Year = datetime.now().year-1
print(Year)
pd.set_option('display.max_columns', None)
df = pd.read_excel(path,index_col=None, header=None, names=["Compañía","Aeropuerto_Base", "Mes", "Movimiento", "País", "Pasajeros"])
df["Año"] = Year
df = df.drop(index=[0, 1, 2, 3])
df["Compañía"].fillna(method='ffill',inplace=True)
df["Aeropuerto_Base"].fillna(method='ffill',inplace=True)
df["Mes"].fillna(method='ffill',inplace=True)
df = df[df["Movimiento"] == "LLEGADA"]

df = df.loc[ df["Aeropuerto_Base"].isin(Aeropuertos), : ]

df["Mes"] = df["Mes"].str.split().str.get(0)
df.set_index("Año",inplace=True)
df = df[df["Mes"] == month]

df = df[['Aeropuerto_Base', "Compañía", 'País', 'Mes', 'Pasajeros']]
df.sort_values(['Aeropuerto_Base', 'País'],
              ascending = [True, True], inplace=True)
print(df)
# print(df["Compañía"].unique())

df.to_csv("C:/Users/lmahmud/Downloads/Aena_%s_%s.csv"%(Year, month))











