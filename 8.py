from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_xpath("/html/body/form/div/div/button")
    button.click() # Нажали на кнопку

    
    new_window = browser.window_handles[1] # выбираем вторую вкладку и присваем ей new_window
    browser.switch_to.window(new_window) # свичим все на 2ю вкладку
    
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
