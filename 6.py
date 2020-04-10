from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math
import os



try:
  
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    elements = browser.find_elements_by_xpath ("/html/body/div/form/div/input[1]")
    for element in elements:
       element.send_keys("Maks")
       elements = browser.find_elements_by_xpath ("/html/body/div/form/div/input[2]")
    for element in elements:
       element.send_keys("Leviga")
       elements = browser.find_elements_by_xpath ("/html/body/div/form/div/input[3]")
    for element in elements:
       element.send_keys("maks@mail.ru")


    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    element = browser.find_element_by_id("file")
    element.send_keys(file_path)

    button = browser.find_element_by_xpath("/html/body/div/form/button")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
