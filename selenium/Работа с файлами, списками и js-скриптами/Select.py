from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

'''
def calc(a,b):
  return (a + b).__str__()
'''

try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Находим на странице число и считываем его
    a_element = browser.find_element(By.ID, "num1")
    b_element = browser.find_element(By.ID, "num2")

    # Атрибут text возвращает текст, который находится между открывающим и закрывающим тегами элемента.
    a = int(a_element.text)
    b = int(b_element.text)

    # Вычисляем значение суммы считанных чисел
    y = str(a + b)

    # Выбираем значение из списка
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(y)  # ищем элемент с текстом = y
    
    # Можно использовать еще два метода:
    # select.select_by_visible_text("text") и select.select_by_index(index).

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
