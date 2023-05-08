import time
from selenium.webdriver.common.by import By
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def close_modal(driver):
    try:
        modal_close_btn = driver.find_element(By.CLASS_NAME, "CCPAModal__StyledCloseButton-sc-10x9kq-2")
        modal_close_btn.click()
    except:
        pass
def load_all_paginated_reviews(driver):
    try:
        load_btn = driver.find_element(By.CLASS_NAME, "PaginationButton__StyledPaginationButton-txi1dr-1")
        while True:
            load_btn.click()
            try:
                time.sleep(.75)
                load_btn = driver.find_element(By.CLASS_NAME, "PaginationButton__StyledPaginationButton-txi1dr-1")
            except:
                break
    except:
        pass
    
def write_to_json_file(file_name, data):
    file = open(file_name, "w")
    file.write(json.dumps(data))
    file.close