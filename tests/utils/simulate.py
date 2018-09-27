from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class Simulate:
    def click_by_xpath(self, driver, xpath):
        elem = driver.find_element_by_xpath(xpath)
        driver.execute_script("arguments[0].click();", elem)

    def click_by_id(self, driver, id):
        elem = driver.find_element_by_id(id)
        driver.execute_script("arguments[0].click();", elem)

    def input_by_xpath(self, driver, xpath, input):
        elem = driver.find_element_by_xpath(xpath)
        elem.clear()
        elem.send_keys(input)

    def input_by_id(self, driver, id, input):
        elem = driver.find_element_by_id(id)
        elem.clear()
        elem.send_keys(input)

    def double_enter(self, driver):
        actions = ActionChains(driver)
        actions.send_keys(Keys.ENTER)
        actions.send_keys(Keys.ENTER)
        actions.perform()

    def down_enter(self, driver, down):
        actions = ActionChains(driver)
        for x in range(int(down)):
            actions.send_keys(Keys.DOWN)
        actions.send_keys(Keys.ENTER)
        actions.perform()
    