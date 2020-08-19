import random
from time import sleep
from selenium import webdriver

driver=webdriver.Chrome('./chromedriver.exe')

for i in range (1,15):
        i=str(i)
        pagina= "https://www.gtainside.com/en/sanandreas/cars-182/latest/"
        url= pagina + i
        driver.get(url) 

        autos = driver.find_elements_by_xpath("//div[contains(@class, 'col-sm-9 col-md-9 col-lg-9')]")

        for auto in autos:
            Nombre=auto.find_element_by_class_name('headline_mod').text 
            print(Nombre)
            
sleep(random.uniform(10.0,15.0))





