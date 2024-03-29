from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Нажимаем кнопку
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Чтобы узнать имя новой вкладки, нужно использовать метод window_handles,
    # который возвращает массив имён всех вкладок. Зная, что в браузере теперь открыто две вкладки,
    # выбираем вторую вкладку:

    new_window = browser.window_handles[1]

    # Также мы можем запомнить имя текущей вкладки, чтобы иметь возможность потом к ней вернуться:
    # first_window = browser.window_handles[0]

    # Переход на новую вкладку браузера
    browser.switch_to.window(new_window)


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
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(4)
    # закрываем браузер после всех манипуляций
    browser.quit()
