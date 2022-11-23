from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Locators.HomePageLocators import iframe
from conftest import *


class Util:
    def find(self, element):
        if element.startswith('//'):
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, element)))
            found_element = driver.find_element(By.XPATH, element)
        else:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, element)))
            found_element = driver.find_element(By.CSS_SELECTOR, element)
        return found_element

    def click_on(self, element):
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, element)))
        driver.find_element(by=By.CSS_SELECTOR, value=element).click()

    def switch_tab_to(self):
        tabs= driver.window_handles
        driver.switch_to.window(tabs[1])

    def frame_switch(css_selector):
        driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR, iframe))


