import time
import math
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
link = "http://suninjuly.github.io/selects1.html"


try:
    browser.get(link)
    num_1 = browser.find_element(By.CSS_SELECTOR, "#num1").text
    num_2 = browser.find_element(By.CSS_SELECTOR, "#num2").text
    find_sum = int(num_1) + int(num_2)
    Select(browser.find_element(By.CSS_SELECTOR, "#dropdown")).select_by_value(str(find_sum))
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(8)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
