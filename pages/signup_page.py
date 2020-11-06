import utilities.custom_logger as cl
from base.basepage import BasePage
import logging

class SignupPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    _signup_link = "//div[@class='ui big button']"
    _username_input = "//input[@id='user_username']"       ### FIX: just use id as the locators
    _password_input = "//input[@id='user_password']"
    _confirmation_input = "//input[@id='user_password_confirmation']"
    _submit_button = "//input[@name='commit']"
    _return_home_button = "//a[@class='text-info']"
    _first_login_link = "//a[@class='ui primary button']"
    _account_dropdown = "//div[@class='ui dropdown item']"
    _account_dropdown_visible = "//div[@class='menu transition visible']"
    _second_login_link = _account_dropdown_visible + "//a[@class='item']"
    _chatroom_link = "//a[@class='active item']"
    _close_message = "//i[@class='close icon']"
    _messages_link = "//a[contains(text(),'Messages')]"

    # locators for verification purposes
    _signup_header = "//h1[contains(text(),'Sign up to MessageMe')]"
    _error_message_displayed = "//div[contains(text(),'There was something wrong with your signup information')]"
    _is_message_closed = "//div[@class='ui {} message transition hidden']"
    _navigate_home = "//h1[contains(text(), 'Welcome to MessageMe - a complete Chat App')]"
    _success_message_displayed = "//div[contains(text(), 'Welcome, {}! Please login to enter the chatroom!')]"
    _chatroom_message_displayed = "//div[contains(text(),'You need to log in to access the chatroom')]"
    _messages_message_displayed = "//div[contains(text(),'You need to log in to access messages')]"


    ### Methods to use features in the signup page ###

    def navigateToSignup(self):
        """
        Navigate from home to signup page
        :return:
        """
        self.elementClick(locator=self._signup_link, locatorType="xpath")

    def clickLoginNavigation(self):
        """
        Navigate from signup page to login page by using login navigation link
        :return:
        """
        self.elementClick(locator=self._first_login_link, locatorType="xpath")

    def clickAccountDropdown(self):
        """
        Click account dropdown to show the dropdown menu
        :return:
        """
        self.elementClick(locator=self._account_dropdown,locatorType="xpath")

    def clickLoginUnderDropdown(self):
        """
        Navigate from signup page to login page by using login link under account dropdown
        :return:
        """
        self.elementClick(locator=self._second_login_link, locatorType="xpath")

    def clickMessagesLink(self):
        """
        Click messages navigation link
        :return:
        """
        self.elementClick(locator=self._messages_link, locatorType="")

    def clickChatroomLink(self):
        """
        Click chatroom navigation link
        :return:
        """
        self.elementClick(locator=self._chatroom_link, locatorType="xpath")

    def inputUsername(self, username):
        """
        Input username into the appropriate textbox
        :param username: String that has user's username
        :return:
        """
        self.sendKeys(data=username, locator=self._username_input, locatorType="xpath")

    def inputPassword(self, password):
        """
        Input password into the appropriate textbox
        :param password: String that has user's password
        :return:
        """
        self.sendKeys(data=password, locator=self._password_input, locatorType="xpath")

    def inputConfirmPassword(self, confirm_password):
        """
        Input password confirmation into the appropriate textbox
        :param confirm_password: String that has user's password confirmation
        :return:
        """
        self.sendKeys(data=confirm_password, locator=self._confirmation_input, locatorType="xpath")

    def clickSignupSubmit(self):
        """
        Click Sign up button to create a new account
        :return:
        """
        self.elementClick(locator=self._submit_button, locatorType="xpath")

    def clickReturnHome(self):
        """
        Click the link to return to the home page
        :return:
        """
        self.elementClick(locator=self._return_home_button, locatorType="xpath")

    def clickCloseMessage(self):
        """
        Click close pop-up message
        :return:
        """
        self.elementClick(locator=self._close_message, locatorType="xpath")

    def cleanUpUsernameAndPassword(self):
        """
        Empty up the textboxes for username, password, and its confirmation
        :return:
        """
        self.getElement(locator=self._username_input, locatorType="xpath").clear()
        self.getElement(locator=self._password_input, locatorType="xpath").clear()
        self.getElement(locator=self._confirmation_input, locatorType="xpath").clear()

    def creatingAccount(self, username, password, password_confirmation):
        """
        Fill username and password, and click sign up
        :param username: String that has user's username
        :param password: String that has user's password
        :return:
        """
        self.inputUsername(username)
        self.inputPassword(password)
        self.inputConfirmPassword(password_confirmation)
        self.clickSignupSubmit()


    ### Methods for verification purposes ###
    
    def verifySignupReached(self):
        """
        Verify that the user reaches sign up page
        :return:
        """
        return self.isElementPresent(locator=self._signup_header, locatorType="xpath")

    def verifyNavigateHome(self):
        """
        Verify that the user reaches home page
        :return:
        """
        return self.isElementPresent(locator=self._navigate_home, locatorType="xpath")

    def verifyMessageDisplayed(self, state, username=""):
        """
        Verify error message is displayed
        :param username: String that indicates if this is error or success message
        :return:
        """
        if state == "success":
            return self.isElementPresent(locator=self._success_message_displayed.format(username), locatorType="xpath")
        elif state == "error":
            return self.isElementPresent(locator=self._error_message_displayed, locatorType="xpath")
        elif state == "chatroomError":
            return self.isElementPresent(locator=self._chatroom_message_displayed, locatorType="xpath")
        elif state == "messagesError":
            return self.isElementPresent(locator=self._messages_message_displayed, locatorType="xpath")

    def verifyMessageClosed(self, state):
        """
        Verify that error message closed
        :param username: String that indicates if this is error or success message
        :return:
        """
        return self.isElementPresent(locator=self._is_message_closed.format(state), locatorType="xpath")

    def verifyDropdownVisible(self):
        """
        Verify that account dropdown menu is visible after click
        :return:
        """
        return self.isElementPresent(locator=self._account_dropdown_visible, locatorType="xpath")


