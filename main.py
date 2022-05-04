from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
try:
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.XPATH, '//h5[@id="price"]'),'$100')
     )
    browser.find_element(By.ID,'book' ).click()
    input1 = browser.find_element(By.XPATH, '//span[@id="input_value"]').text
    browser.find_element(By.XPATH, '//input[@id="answer"]').send_keys(calc(input1))
    button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)  #прокрутить вниз
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()