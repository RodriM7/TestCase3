import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(executable_path="C:\Program Files\Google\Chrome\Application\chromedriver.exe", options=options)
driver.get("https://lavandanatural.com/")
time.sleep(2)

icono = driver.find_element(By.ID, "auth")
icono.click()
time.sleep(1)

login = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[4]/div[1]/header/div/div[2]/div[2]/div[1]/div/a[2]")
login.click()
time.sleep(3)

mail = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[5]/div/div[4]/form/div[1]/input")
mail.send_keys("rmunoz_probar@yahoo.com")
time.sleep(2)

passw = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[5]/div/div[4]/form/div[2]/input")
passw.send_keys("probar123456")
passw.send_keys(Keys.ENTER) # Inicia sesion
time.sleep(2)

inicio = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[4]/div[1]/header/div/ul/li[1]/a")
inicio.click()
time.sleep(2)

barra = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[4]/div[1]/header/div/div[2]/div[1]/form/input")
barra.click()
barra.send_keys("jabon") # Busqueda de producto en la barra de busqueda
time.sleep(5)

primero = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[4]/div[1]/header/div/div[2]/div[1]/div/ul/li[1]/a")
primero.click() # Selecciona el primer producto 
time.sleep(3)

cantidad = driver.find_element(By.ID, "quantity")
cantidad.clear()
cantidad.send_keys("3") # Agregar 3 productos al carro
cantidad.send_keys(Keys.ENTER)
time.sleep(3)

requirement = ()    
labelObtained = ()      

def compareLabels():
    if requirement in labelObtained:
        print("Pass")
    else:
        print("Fail")

#validar que se agreguen 3 productos y que se visualicen en el carrito
linkCantidad = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[5]/div[1]/div[2]/div/div[2]/div/form/div[2]/div[1]/label")   

labelCantidad =  driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[5]/div[1]/div[2]/div/div[2]/div/form/div[2]/div[1]/label").text

labelObtained = labelCantidad

print(labelObtained)

requirement = 'CANTIDAD'

compareLabels()

finalizar = driver.find_element(By.XPATH, "/html/body/div[3]/form/div/div[4]/div/div[8]/div[3]/input")
finalizar.click() # finalizar la compra
time.sleep(3)

cerrar = driver.find_element(By.XPATH, "/html/div/div[2]/div[1]")
cerrar.click()
time.sleep(3)

checkout = driver.find_element(By.ID, "shippingAddress.zipcode")
checkout.click() # Se visualiza el checkout de la pagina
checkout.send_keys("5010")
time.sleep(3)

driver.close()