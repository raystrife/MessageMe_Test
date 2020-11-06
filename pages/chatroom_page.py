import utilities.custom_logger as cl
from base.basepage import BasePage
import logging

class ChatroomPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    _account_dropdown = "//div[@class='ui dropdown item']"
    _logout_link = "//a[contains(text(),'Logout')]"
    # messages_link = ""
    _chatroom_link = "//a[contains(text(),'Chatroom')]"
    _chat_input = "//input[@id='message_body']"
    _chat_submit_button = "//button[@name='button']"
    _home_link = "//a[contains(text(),'Home')]"
    _messages_link = "//div[@class='ui inverted vertical menu']//a[contains(text(),'Messages')]"
    _friends_link = "//a[contains(text(),'Friends')]"

    # locators for verifications
    _reach_chatroom = "//i[@class='circular orange coffee icon']"
    _reach_messages = ""        # Update this later
    _reach_friends = ""         # Update this later
    _new_chat_displayed = "//div[contains(em/following-sibling::text(), '{}') and contains(em, '{}')]"
    _account_dropdown_visible = "//div[@class='menu transition visible']"

    def clickChatroomNavigationLink(self):
        """
        Click the chatroom link on the navigation bar
        :return:
        """
        self.elementClick(locator=self._chatroom_link, locatorType="xpath")

    def clickHomeLink(self):
        """
        Click the home link on the navigation menu
        :return:
        """
        self.elementClick(locator=self._home_link, locatorType="xpath")

    def clickMessagesLink(self):
        """
        Click the messages link on the navigation menu
        :return:
        """
        self.elementClick(locator=self._messages_link, locatorType="xpath")

    def clickFriendsLink(self):
        """
        Click the friends link on the navigation menu
        :return:
        """
        self.elementClick(locator=self._friends_link, locatorType="xpath")

    def fillChatInput(self, message):
        """
        Fill the chat input with user's message
        :param message: a String that contains the user's message
        :return:
        """
        self.sendKeys(data=message, locator=self._chat_input, locatorType="xpath")

    def submitChatByClickingSubmit(self):
        """
        Click submit to send the chat message
        :return:
        """
        self.elementClick(locator=self._chat_submit_button, locatorType="xpath")

    def submitChatByPressingEnter(self):
        """
        Press ENTER to send the chat message
        :return:
        """
        self.pressEnter(locator=self._chat_input, locatorType="xpath")

    def cleanUpChatInput(self):
        """
        Empty up the chat input
        :return:
        """
        self.getElement(locator=self._chat_input, locatorType="xpath").clear()

    def writeMessage(self, message, submitMethod):
        """
        Write a message and submit it
        :param message: a String that contains the user's message
        :param submitMethod: a String that shows how the user is submitting the message: "enter" or "click"
        :return:
        """
        self.fillChatInput(message)
        if (submitMethod == "enter"):
            self.submitChatByPressingEnter()
        elif (submitMethod == "click"):
            self.submitChatByClickingSubmit()

    def clickAccountDropdown(self):
        """
        Click the account dropdown
        :return:
        """
        self.elementClick(locator=self._account_dropdown, locatorType="xpath")

    def clickLogOut(self):
        """
        Click log out
        :return:
        """
        self.elementClick(locator=self._logout_link, locatorType="xpath")


    def verifyChatroomReached(self):
        """
        Verify the users are able to access the chatroom after login
        :return:
        """
        return self.isElementPresent(locator=self._reach_chatroom, locatorType="xpath")

    def verifyMessagesReached(self):
        """
        Verify the users are able to access the messages page after login
        :return:
        """
        return self.isElementPresent(locator=self._reach_messages, locatorType="xpath")

    def verifyFriendsReached(self):
        """
        Verify the users are able to access the friends page after login
        :return:
        """
        return self.isElementPresent(locator=self._reach_friends, locatorType="xpath")

    def verifyNewChatDisplayed(self, username, chat):
        """
        Verify that the new message that is submitted is displayed on the chat box
        :return:
        """
        chat_message = ": " + chat
        return self.isElementPresent(locator=self._new_chat_displayed.format(chat_message, username),
                                     locatorType="xpath")

    def verifyEmptyChatField(self):
        """
        Verify that the chat field is empty after the message is submitted
        :return:
        """
        return self.isInputFieldClear(locator=self._chat_input, locatorType="xpath")

    def verifyAccountDropdownOpen(self):
        """
        Verify that the account dropdown opens after it is clicked
        :return:
        """
        return self.isElementPresent(locator=self._account_dropdown_visible, locatorType="xpath")

