from seleniumwire import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import json
import re

chrome_options = webdriver.ChromeOptions()

service = Service(
    ChromeDriverManager().install()
)

driver = webdriver.Chrome(
    service=service, options=chrome_options
)

keyword = 'Sushi'

driver.get(f'https://www.google.com/maps/search/${keyword}/')

try:
    WebDriverWait(Driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"form:nth-child(2)"))).click()
except Exception:
    pass

time.sleep(60)