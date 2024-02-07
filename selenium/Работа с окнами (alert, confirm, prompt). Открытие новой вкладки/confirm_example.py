from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Нажимаем кнопку
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Переключение на окно confirm и нажатие кнопки подтверждения
    confirm = browser.switch_to.alert
    confirm.accept()

    # Для отказа используется:
    # confirm.dismiss()

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

    """
    alert окно с одной кнопкой подтверждения
    confirm окно с двумя кнопками: подтвердить и отказаться
    prompt окно с полем для ввода и двумя кнопками: подтвердить и отказаться
    
    примеры еще:
    alert = browser.switch_to.alert
    alert.accept()
    Чтобы получить текст из alert, используйте свойство text объекта alert:
    
    alert = browser.switch_to.alert
    alert_text = alert.text
    
    Третий вариант модального окна — prompt — имеет дополнительное поле для ввода текста.
    Чтобы ввести текст, используйте метод send_keys():

    prompt = browser.switch_to.alert
    prompt.send_keys("My answer")
    prompt.accept()
    """
