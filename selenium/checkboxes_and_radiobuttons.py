from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Находим на странице число и считываем его
    x_element = browser.find_element(By.CSS_SELECTOR, "span[id='input_value'].nowrap")
    x = x_element.text    # Атрибут text возвращает текст, который находится между открывающим и закрывающим тегами элемента.

    # Вычисляем значение по формуле, описанной выше
    y = calc(x)

    # Вводим значение в поле
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    # Cнять/поставить галочку в элементе типа checkbox
    option1 = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    option1.click()

    # Выбрать опцию из группы radiobuttons
    option2 = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    option2.click()

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
