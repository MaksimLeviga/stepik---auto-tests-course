from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_xpath("/html/body/form/div/div/button")
    button.click() # Нажали на кнопку
    
    alert = browser.switch_to.alert
    alert.accept() # Подтверждаем алерт

    # ждем загрузки страницы
    time.sleep(1)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    elements = browser.find_elements_by_id ("answer")
    for element in elements:
       element.send_keys(y) # нашли на странице х и ввели ответ в поле
       
    button = browser.find_element_by_xpath("/html/body/form/div/div/button")
    button.click() # Нажали на кнопку
 

    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
