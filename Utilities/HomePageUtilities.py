import time
from Config.Configdata import shoes1
from Locators.HomePageLocators import *
from Utilities.CommonPageUtilities import *
from conftest import driver


class HomePageFunctions:
    def search_bar(self):
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, search_field)))
        driver.find_element(By.CSS_SELECTOR, search_field).send_keys(shoes1)
        driver.find_element(By.CSS_SELECTOR, search_field).send_keys(u'\ue007')
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, shoes)))
        product = driver.find_elements(By.CSS_SELECTOR, shoes)
        product[0].click()

    def select_size(self):
        # WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, shoes_size)))
        time.sleep(5)
        Util().switch_tab_to()
        driver.find_element(By.XPATH, shoes_size).click()

    def add_to_cart(self):
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, add_to_bag)))
        driver.find_element(By.CSS_SELECTOR, add_to_bag).click()

    def click_to_cart(self):
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, view_cart)))
        driver.find_element(By.CSS_SELECTOR, view_cart).click()

    def procced_to_buy(self):
        # WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, procced_to_buy)))
        time.sleep(5)
        Util().frame_switch()
        driver.find_element(By.CSS_SELECTOR, procced_to_buy).click()

    def final_order(self):
        self.search_bar()
        self.select_size()
        self.add_to_cart()
        self.click_to_cart()
        self.procced_to_buy()
