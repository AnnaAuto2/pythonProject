from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
button = browser.find_element(By.TAG_NAME, "button")

# Так как кнопка оказалась перекрыта другим элементом, то нам нужно проскроллить.
# Мы дополнительно передали в метод scrollIntoView аргумент true,
# чтобы элемент после скролла оказался в области видимости.
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()