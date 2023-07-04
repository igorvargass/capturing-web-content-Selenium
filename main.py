from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

#abrindo navegador
driver = webdriver.Chrome()
driver.get("http://10.3.198.54:81/login.asmx")
print(bool(False))
#localizando validador de página
try:
    element = WebDriverWait(driver, timeout=10).until(
        expected_conditions.presence_of_element_located((By.ID, "content"))
    )
    print(bool(5))
except:
    print("erro")