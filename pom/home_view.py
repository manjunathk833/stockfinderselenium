import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class home_view():
    search_xpath = '//*[@id="search-stock-input"]'
    search_input = 'ITC'
    itc_xpath = '//*[@id="stock-suggestion-ITC Ltd"]/a'

    def __init__(self, driver):
        self.driver = driver

    def search_stock(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, self.search_xpath)))
        self.driver.find_element(By.XPATH, self.search_xpath).send_keys(self.search_input)

    def click_res(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, self.itc_xpath)))
        self.driver.find_element(By.XPATH, self.itc_xpath).click()
        time.sleep(3)