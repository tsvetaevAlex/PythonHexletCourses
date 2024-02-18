from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

# Initialize Chrome driver instance
driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))

# Navigate to the url
driver.get('http://yandex.ru')
search_request = driver.find_element_by_id('')
# input class ="arrow__input mini-suggest__input"
# Close the driver
driver.quit()