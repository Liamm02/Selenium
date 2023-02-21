from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, NoSuchWindowException,\
    TimeoutException, WebDriverException
from Constants import *
from selenium.webdriver import ChromeOptions
import time


def Download_Document():
    try:

        options = Options()

        options.add_argument('--disable-extensions')
        options.add_argument("--window-size=1600,768")
        binary = FirefoxBinary("C:/Program Files/Mozilla Firefox/firefox.exe")
        caps = DesiredCapabilities().FIREFOX
        caps["marionette"] = True

        driver = webdriver.Firefox(firefox_binary=binary, options=options, capabilities=caps)

        driver.set_page_load_timeout(180)
        driver.get(AENA)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button.ecix-bold ecix-font-1-2em elix-accordion-btn-primary elix-deny-all-hidden-2".replace(" ", ".")))).click()

        lnks=driver.find_elements(By.CLASS_NAME, "nav-link btn azul centrado".replace(" ", "."))
        lnks[3].click()

        print("Esperando respuesta de Aena")
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'EurolandTool')))
        # WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.ID, 'EurolandTool')))
        print("here")

        time.sleep(20)
        action = ActionChains(driver)
        action.move_by_offset(300, 445).double_click().perform()
        action.move_by_offset(-300, -445).perform()

        # driver.switch_to.default_content()

        driver.execute_script("window.scrollTo(0, 600);")
        time.sleep(1)
        action.move_by_offset(180,470).click().perform()
        action.move_by_offset(-180,-470).perform()
        driver.execute_script("window.scrollTo(0, 150);")

        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'EurolandTool')))
        WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.ID, 'EurolandTool')))
        driver.switch_to
        time.sleep(10)

        print("Filtrando información")
        #Aeropuerto base
        # action.move_by_offset(250,280).click_and_hold().perform()
        # action.move_by_offset(250,20).release()
        driver.switch_to.default_content()
        fr = driver.find_elements(By.XPATH, "//iframe")
        driver.switch_to.frame(fr[1])
        el = driver.find_elements(By.CLASS_NAME, "item.unit.ic12")

        el2 = driver.find_elements(By.CLASS_NAME, "mstrmojo-VIPanel.mstrmojo-VIPanelPortlet")

        for e in el2:
            print(e.get_attribute("id"))

        action.drag_and_drop(el[0],el2[2]).perform()
        el2 = driver.find_elements(By.CLASS_NAME, "mstrmojo-VIPanel.mstrmojo-VIPanelPortlet")
        for e in el2:
            print(e.get_attribute("id"))
        time.sleep(1)
        # action.drag_and_drop(el[1],el2[2]).perform()
        # time.sleep(1)
        # action.drag_and_drop(el[3],el2[2]).perform()
        # time.sleep(1)
        # action.drag_and_drop(el[5],el2[2]).perform()
        # time.sleep(1)
        # action.drag_and_drop(el[6],el2[2]).perform()
        # time.sleep(1)
        # action.drag_and_drop(el[7],el2[2]).perform()


        # action.click_and_hold(on_element=el[0]).perform()
        # action.release(on_element=el2[1])
        time.sleep(1)

        # time.sleep(6)
        # #Año
        # action.move_by_offset(0, 30).double_click().perform()
        # time.sleep(3)
        # #Compañía
        # action.move_by_offset(0, 60).double_click().perform()
        # time.sleep(3)
        # #Mes
        # action.move_by_offset(0, 60).double_click().perform()
        # time.sleep(4)
        # #Movimiento
        # action.move_by_offset(0, 20).double_click().perform()
        # time.sleep(4)
        # #Pais
        # action.move_by_offset(0, 30).double_click().perform()
        # time.sleep(4)
        #
        # #Descarga de archivo.
        # action.move_by_offset(-300, -475).perform()
        # action.move_by_offset(1360, 345).perform()
        # action.click().perform()
        # time.sleep(1)
        # action.move_by_offset(0, 50).perform()
        # action.click().perform()
        # time.sleep(1)
        # action.move_by_offset(-150, 5).perform()
        # action.click().perform()
        #
        # print("Esperando por la descarga para procesar datos...")
        # time.sleep(15)
        # driver.close()
        # return 0

    # except NoSuchElementException:
    #     print("Algo fue mal, reintentando...")
    #     return 1
    # except ElementNotInteractableException:
    #     print("Algo fue mal, reintentando...")
    #     return 1
    except NoSuchWindowException:
        print("La ventana se cerró de forma inesperada, reintentando...")
        return 1
    # except TimeoutException:
    #     print("La paginá tardó demasiado en cargar, reintentando...")
    #     return 1
    # except WebDriverException:
    #     print("Algo fue mal, reintentando...")
    #     return 1
    # except IndexError:
    #     print("Descarga fallida, reintentando")
    #     return 1
