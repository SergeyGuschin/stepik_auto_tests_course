import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import os

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
link = "http://suninjuly.github.io/file_input.html"


try:
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, ".form-control").send_keys("Sergey")
    browser.find_element(By.CSS_SELECTOR, "input[name='lastname']").send_keys("Me")
    browser.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys("test@test.qa")
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'test.txt')  # добавляем к этому пути имя файла
    # print(file_path)
    browser.find_element(By.CSS_SELECTOR, "#file").send_keys(file_path)
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(8)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
