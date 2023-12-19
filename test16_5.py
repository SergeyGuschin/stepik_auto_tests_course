import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


link = "http://suninjuly.github.io/registration2.html"

try:
    # browser = webdriver.Chrome()
    browser.get(link)
    # Ваш код, который заполняет обязательные поля
    browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your first name']").send_keys("FirstName")
    browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your last name']").send_keys("LastName")
    browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your email']").send_keys("email@test.qa")
    browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your first name']").send_keys("+1456987456")
    browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your first name']").send_keys("1st street, Test City, 98765")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

