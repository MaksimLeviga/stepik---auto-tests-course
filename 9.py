from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    
    browser = webdriver.Chrome()
    
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    price = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100") # указали где и что искать для until 
        )
    
    button = browser.find_element_by_id("book") # кнопка
    button.click()

    # assert "$100" in price.text

    

    x_element = browser.find_element_by_id("input_value") # забрали х из строки
    x = x_element.text
    y = calc(x)
    elements = browser.find_elements_by_id ("answer") # ввели значение у в ответ
    for element in elements:
       element.send_keys(y)

    button_2 = browser.find_element_by_id("solve") # нажали submit
    button_2.click()
    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()
