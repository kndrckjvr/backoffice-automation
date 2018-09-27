from config.configs import Configs
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class Simulate:
    # click_by_path Function
    # function to simulate a click action and finding the element using its xPath
    # params xpath
    # xpath ([xPath] Element's xPath)
    def click_by_xpath(self, xpath):
        elem = Configs.drv.find_element_by_xpath(xpath)
        Configs.drv.execute_script("arguments[0].click();", elem)

    # click_by_id Function
    # function to simulate a click action and finding the element using its id
    # params id
    # id ([id] Element's Id)
    def click_by_id(self, id):
        elem = Configs.drv.find_element_by_id(id)
        Configs.drv.execute_script("arguments[0].click();", elem)

    # click_by_link Function
    # function to simulate a click action using the link's text
    # params text
    # text ([Link Text] Link's Text)
    def click_by_link(self, text):
        elem = Configs.drv.find_element_by_link_text(text)
        Configs.drv.execute_script("arguments[0].click();", elem)

    # input_by_xpath Function
    # function to simulate an input using the element's xPath
    # params xpath input
    # xpath ([xPath] Element's xPath)
    # input ([Text Input] Text input)
    def input_by_xpath(self, xpath, input):
        elem = Configs.drv.find_element_by_xpath(xpath)
        elem.clear()
        elem.send_keys(input)

    # input_by_id Function
    # function to simulate an input using the element's Id
    # params id input
    # id ([id] Element's Id)
    # input ([Text Input] Text input)
    def input_by_id(self, id, input):
        elem = Configs.drv.find_element_by_id(id)
        elem.clear()
        elem.send_keys(input)

    # double_enter Function
    # function to simulate a Double Enter
    def double_enter(self):
        actions = ActionChains(Configs.drv)
        actions.send_keys(Keys.ENTER)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        
    # down_enter Function
    # function to simulate dynamically pressing down arrow and enter simultaenously
    # params down
    # down ([DownArrow Count] How many time the down arrow will be pressed)
    def down_enter(self, down):
        actions = ActionChains(Configs.drv)
        for x in range(int(down)):
            actions.send_keys(Keys.DOWN)
        actions.send_keys(Keys.ENTER)
        actions.perform()
    