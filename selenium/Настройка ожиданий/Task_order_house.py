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
    # говорим WebDriver искать каждый элемент в течение 5 секунд
    browser.implicitly_wait(5)

    browser.get("https://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 12 секунд появления дома с ценой = 100
    time_wait = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "100"))

    # Нажимаем кнопку
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Находим на новой открывшейся странице число и считываем его
    x_element = browser.find_element(By.ID, "input_value")
    # Сохраняем в переменную x значение атрибута найденного ранее элемента (get_attribute)
    x = x_element.text
    # Вычисляем значение по формуле, описанной выше
    y = calc(x)

    # Вводим значение в поле
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    # Отправляем заполненную форму
    button2 = browser.find_element(By.ID, "solve")
    button2.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


