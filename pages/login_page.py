import utilities.custom_logger as cl
from base.basepage import BasePage
import logging

class LoginPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    _username_input = "//input[@id='session_username']"
    _password_input = "//input[@id='session_password']"
    _login_button = "//button[@name='button']"
    _first_login_link = "//a[@class='ui primary button']"
    _account_dropdown = "//div[@class='ui dropdown item']"
    _account_dropdown_visible = "//div[@class='menu transition visible']"
    _second_login_link = _account_dropdown_visible + "//a[@class='item']"
    _chatroom_link = "//a[@class='active item']"
    _close_message = "//i[@class='close icon']"
    # _messages_link = "Messages"     ### find by partial text?

    # locators for verification
    _reach_login = "//h1[contains(text(),'Welcome to MessageMe - a complete Chat App')]"
    _chatroom_message_displayed = "//div[contains(text(), 'You need to log in to access the chatroom')]"
    _messages_message_displayed = "//div[contains(text(),'You need to log in to access messages')]"
    _error_message_displayed = "//div[contains(text(),'There was something wrong with your login information')]"
    _success_message_displayed = "//div[contains(text(),'You have successfully logged in')]"
    _logout_message_displayed = "//div[contains(text(),'You have successfully logged out')]"
    _is_message_closed = "//div[@class='ui {} message transition hidden']"
    _reach_chatroom = "//i[@class='circular orange coffee icon']"


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

    def clickLoginSubmit(self):
        """
        Click Login button to create a new account
        :return:
        """
        self.elementClick(locator=self._login_button, locatorType="xpath")

    def clickCloseMessage(self):
        """
        Click close pop-up message
        :return:
        """
        self.elementClick(locator=self._close_message, locatorType="xpath")

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

    # def clickMessagesLink(self):
    #     """
    #     Click messages navigation link
    #     :return:
    #     """
    #     self.elementClick(locator=self._messages_link, locatorType="")

    def clickChatroomLink(self):
        """
        Click chatroom navigation link
        :return:
        """
        self.elementClick(locator=self._chatroom_link, locatorType="xpath")

    def loggingAccount(self, username, password):
        """
        Fill username and password, and click sign up
        :param username: String that has user's username
        :param password: String that has user's password
        :return:
        """
        self.inputUsername(username)
        self.inputPassword(password)
        self.clickLoginSubmit()


    def verifyLoginPageReached(self):
        """
        Verify the user navigates to the login page successfully
        :return:
        """
        return self.isElementPresent(locator=self._reach_login, locatorType="xpath")

    def verifyDropdownVisible(self):
        """
        Verify that account dropdown menu is visible after click
        :return:
        """
        return self.isElementPresent(locator=self._account_dropdown_visible, locatorType="xpath")

    def verifyMessageDisplayed(self, state):
        """
        Verify error message is displayed
        :param username: String that indicates if this is error or success message
        :return:
        """
        if state == "error":
            return self.isElementPresent(locator=self._error_message_displayed, locatorType="xpath")
        elif state == "success":
            return self.isElementPresent(locator=self._success_message_displayed, locatorType="xpath")
        elif state == "chatroomError":
            return self.isElementPresent(locator=self._chatroom_message_displayed, locatorType="xpath")
        elif state == "messageError":
            return self.isElementPresent(locator=self._messages_message_displayed, locatorType="xpath")
        elif state == "logout":
            return self.isElementPresent(locator=self._logout_message_displayed, locatorType="xpath")

    def verifyMessageClosed(self, state):
        """
        Verify that error message closed
        :param username: String that indicates if this is error or success message
        :return:
        """
        return self.isElementPresent(locator=self._is_message_closed.format(state), locatorType="xpath")

    def verifyNavigateChatroom(self):
        """
        Verify that successful login navigates the user to the chatroom page
        :return:
        """
        return self.isElementPresent(locator=self._reach_chatroom, locatorType="xpath")



