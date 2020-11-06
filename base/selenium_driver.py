from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
from traceback import print_stack
import utilities.custom_logger as cl
import logging
import time
import os

class SeleniumDriver():
    log = cl.customLogger(logging.INFO)

    def __init__(self, driver):
        self.driver = driver

    def screenShot(self, resultMessage):
        """
        Takes screenshot of the current open web page
        :param resultMessage: a str that contains the error message
        """
        fileName = resultMessage + "." + str(round(time.time() * 1000)) + ".png"
        screenshotDirectory = "../screenshots/"
        relativeFileName = screenshotDirectory + fileName
        currentDirectory = os.path.dirname(__file__)
        destinationFile = os.path.join(currentDirectory, relativeFileName)
        destinationDirectory = os.path.join(currentDirectory, screenshotDirectory)

        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationDirectory)
            self.log.info("Screenshot save to directory: " + destinationFile)
        except:
            self.log.error("### Exception Occurred")
            print_stack()

    def resizeWindow(self, width, height):
        """
        Set the size of the browser window
        :param width: the width of the window
        :param height: the height of the window
        """
        self.driver.set_window_size(width, height)

    def getTitle(self):
        """
        Get the title of the current web page
        :return: the title of the web page
        """
        return self.driver.title

    def getByType(self, locatorType):
        """
        Determine the locator type to locate the element
        :param locatorType: the locator type
        :return: the locator type from the By class
        """
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        else:
            self.log.info("Locator type" + locatorType + " not correct/supported")
        return False

    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info("Element Found with locator: " + locator + " locatorType: " + locatorType)
        except:
            self.log.info("Element not found with locator" + locator + " locatorType: " + locatorType)
        return element

    def getElementList(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_elements(byType, locator)
            self.log.info("Element list Found with locator: " + locator + " locatorType: " + locatorType)
        except:
            self.log.info("Element list not found with locator" + locator + " locatorType: " + locatorType)
        return element

    def elementClick(self, locator="", locatorType="id", element=None):
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            element.click()
            self.log.info("Clicked on element with locator: " + locator + " locatorType: " + locatorType)
        except:
            self.log.info("Cannot click on the element with locator: " + locator + " locatorType: " + locatorType)
            print_stack()

    def elementHover(self, locator="", locatorType="id", element=None):
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            self.log.info("Hover over element with locator: " + locator + " locatorType: " + locatorType)
        except:
            self.log.info("Cannot hover over the element with locator " + locator + " locatorType: " + locatorType)
            print_stack()

    def sendKeys(self, data, locator="", locatorType="id", element=None):
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            element.send_keys(data)
            self.log.info("Clicked on element with locator: " + locator + " locatorType: " + locatorType)
        except:
            self.log.info("Cannot send data on the element with locator: " + locator + " locatorType: " + locatorType)
            print_stack()

    def getText(self, locator="", locatorType="id", element=None, info=""):
        try:
            if locator:
                self.log.debug("in locator condition")
                element = self.getElement(locator, locatorType)
            self.log.debug("Before finding text")
            text = element.text
            self.log.debug("After finding element, size is: " + str(len(text)))
            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text) != 0:
                self.log.info("Getting text on element :: " + info)
                self.log.info("The text is :: '" + text + "'")
                text = text.strip()
        except:
            self.log.error("Failed to get text on element" + info)
            print_stack()
            text = None

    def isElementPresent(self, locator="", locatorType="id", element=None):
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            if element is not None:
                self.log.info("Element present with locator: " + locator + " locatorType: " + locatorType)
                return True
            else:
                self.log.info("Element not present with locator: " + locator + " locatorType: " + locatorType)
                return False
        except:
            self.log.info("Element not found")
            return False

    def isElementDisplayed(self, locator="", locatorType="id", element=None):
        isDisplayed = False
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            if element is not None:
                isDisplayed = element.is_displayed()
                self.log.info("Element is displayed with locator: " + locator + " locatorType: " + locatorType)
            else:
                self.log.info("Element not displayed with locator: " + locator + " locatorType: " + locatorType)
            return isDisplayed
        except:
            print("Element not found")
            return False

    def getElementAttribute(self, attribute="", locator="", locatorType="id", element=None):
        attributeResult = ""
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            if element is not None:
                attributeResult = element.get_attribute(attribute)
                self.log.info("Attribute: " + attribute + " is found for locator: " + locator +
                              " locatorType: " + locatorType)
            else:
                self.log.info("Attribute: " + attribute + " is not found for locator: " + locator +
                              " locatorType: " + locatorType)
            return attributeResult
        except:
            print("Element not found")
            return False

    def getCSSValue(self, property="", locator="", locatorType="id", element=None):
        cssResult = ""
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            if element is not None:
                cssResult = element.value_of_css_property(property)
                self.log.info("CSS property: " + property + " is found for locator: " + locator +
                              " locatorType: " + locatorType)
            else:
                self.log.info("CSS property: " + property + " is not found for locator: " + locator +
                              " locatorType: " + locatorType)
            return cssResult
        except:
            print("Element not found")
            return False

    def elementPresenceCheck(self, locator, byType):
        try:
            elementList = self.driver.find_elements(byType, locator)
            if len(elementList) > 0:
                self.log.info("Element Found")
                return True
            else:
                self.log.info("Element not found")
                return False
        except:
            self.log.info("Element not found")
            return False

    def waitForElement(self, locator, locatorType="id", timeout=10, pollFrequency=0.5):
        element = None
        try:
            byType = self.getByType(locatorType)
            self.log.info("Waiting for maximum ::" + str(timeout) + " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType, "stopFilter_stops-0")))
            self.log.info("Element appeared on the web page")
        except:
            self.log.info("Element not appeared on the web page")
            print_stack()
        return element

    def scrollFindElement(self, elementLocator):
        element = self.getElement(locator="//h1[contains(text(),'" + elementLocator + "')]",locatorType="xpath")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(2)

    def pressEnter(self, locator="", locatorType="id", element=None):
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            element.send_keys(Keys.ENTER)
            self.log.info("Pressed ENTER on element with locator: " + locator + " locatorType: " + locatorType)
        except:
            self.log.info("Cannot press ENTER on the element with locator: " + locator + " locatorType: " + locatorType)
            print_stack()

    def isInputFieldClear(self, locator="", locatorType="id", element=None):
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            is_empty = element.get_attribute("value")
            self.log.info("Pressed ENTER on element with locator: " + locator + " locatorType: " + locatorType)
            if (is_empty == ""):
                return True
            else:
                return False
        except:
            self.log.info("Cannot press ENTER on the element with locator: " + locator + " locatorType: " + locatorType)
            print_stack()
            return False