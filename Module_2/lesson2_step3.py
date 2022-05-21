from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    #link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = int((browser.find_element(By.ID, 'num1')).text)
    y = int((browser.find_element(By.ID, 'num2')).text)
    z = x + y

    select = Select(browser.find_element(By.ID, 'dropdown'))
    select.select_by_value(str(z))

    option = browser.find_element(By.CLASS_NAME, 'btn-default')
    option.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()