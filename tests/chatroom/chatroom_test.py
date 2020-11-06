from pages.chatroom_page import ChatroomPage
from pages.login_page import LoginPage
from utilities.teststatus import TestStatus
import unittest
import pytest
import utilities.util as util
from random import randint

@pytest.mark.usefixtures("oneTimeSetup", "setUp")
class ChatroomTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetup):
        self.chatroom = ChatroomPage(self.driver)
        self.login = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.util = util.Util()

    @pytest.mark.run(order=1)
    def test_useChatroomNavigationLink(self):
        """
        CHAT_001: Verify clicking "Chatroom" open the appropriate pages
        :return:
        """
        username = "test1"
        password = "testpassword"

        # Verify successfully navigates to the chatroom
        self.login.loggingAccount(username, password)
        result_reachChatroom = self.chatroom.verifyChatroomReached()
        self.ts.mark(result_reachChatroom, "Successfully reach the chatroom after logging in")
        self.util.sleep(sec=1)

        # Verify clicking chatroom link navigates the user to the chatroom page
        self.chatroom.clickChatroomNavigationLink()
        result_reachChatroom = self.chatroom.verifyChatroomReached()
        self.ts.markFinal("test_useChatroomNavigationLink", result_reachChatroom,
                          "Successfully reach the chatroom after logging in")
        self.util.sleep(sec=2)

    @pytest.mark.run(order=2)
    def test_useMessagesNavigationLink(self):
        """
        CHAT_001: Verify clicking "Messages" navigation link open the appropriate pages
        :return:
        """
        # Verify clicking messages link navigates the user to the messages page
        self.chatroom.clickMessagesNavigationLink()
        result_reachMesssages = self.chatroom.verifyMessagesReached()
        self.ts.markFinal("test_useMessagesNavigationLink", result_reachMesssages,
                          "Successfully reach the messages page after logging in")
        self.util.sleep(sec=2)

    @pytest.mark.run(order=3)
    def test_useLinksUnderNavigationMenu(self):
        """
        CHAT_002: Verify clicking "Home", "Messages", and "Friends" open the appropriate pages
        :return:
        """
        # Verify successfully navigates to messages page
        self.chatroom.clickMessagesLink()
        result_reachMessages = self.chatroom.verifyMessagesReached()
        self.ts.mark(result_reachMessages, "Successfully reach the messages page after logging in")
        self.util.sleep(sec=1)

        # Verify successfully navigates to friends page
        self.chatroom.clickFriendsLink()
        result_reachFriends = self.chatroom.verifyFriendsReached()
        self.ts.mark(result_reachFriends, "Successfully reach the friends page after logging in")
        self.util.sleep(sec=1)

        # Verify successfully navigates to the chatroom
        self.chatroom.clickHomeLink()
        result_reachChatroom = self.chatroom.verifyChatroomReached()
        self.ts.markFinal("test_useLinksUnderNavigationMenu", result_reachChatroom,
                          "Successfully reach the friends page after logging in")
        self.util.sleep(sec=2)

    @pytest.mark.run(order=4)
    def test_submitMessageByClickingAndPressingEnter(self):
        """
        CHAT_004: Verify chatting will display the message on the container under the user's name
        :return:
        """
        message = "hello" + str(randint(0,10000000000))
        username = "test1"

        # Verify message is displayed after clicking submit
        self.chatroom.writeMessage(message, "click")
        result_messageDisplayed = self.chatroom.verifyNewChatDisplayed(username, message)
        self.ts.mark(result_messageDisplayed, "The message is displayed on the chat box after clicking submit")

        # Verify the chat input field is empty after clicking submit
        result_emptyField = self.chatroom.verifyEmptyChatField()
        self.ts.mark(result_emptyField, "The chat input field is empty after clicking submit")
        self.chatroom.cleanUpChatInput()
        self.util.sleep(sec=1)

        message = "world" + str(randint(0,10000000000))
        # Verify message is displayed after pressing ENTER
        self.chatroom.writeMessage(message, "enter")
        result_messageDisplayed = self.chatroom.verifyNewChatDisplayed(username, message)
        self.ts.mark(result_messageDisplayed, "The message is displayed on the chat box after pressing enter")

        # Verify the chat input field is empty after pressing ENTER
        result_emptyField = self.chatroom.verifyEmptyChatField()
        self.ts.markFinal("test_submitMessageByClickingAndPressingEnter", result_emptyField,
                          "The chat input field is empty after pressing ENTER")
        self.chatroom.cleanUpChatInput()
        self.util.sleep(sec=2)

    @pytest.mark.run(order=5)
    def test_submitEmptyMessage(self):
        """
        CHAT_007: Verify empty chat message will not show up in the chatbox
        :return:
        """
        message = "   "
        username = "test1"

        # Verify message is displayed after clicking submit
        self.chatroom.writeMessage(message, "click")
        result_messageDisplayed = self.chatroom.verifyNewChatDisplayed(username, message)
        self.ts.mark((not result_messageDisplayed),
                     "Empty message is not displayed on the chat box after clicking submit")
        self.util.sleep(sec=1)

        # Verify message is displayed after pressing ENTER
        self.chatroom.writeMessage(message, "enter")
        result_messageDisplayed = self.chatroom.verifyNewChatDisplayed(username, message)
        self.ts.markFinal("test_submitEmptyMessage", (not result_messageDisplayed),
                          "Empty message is not displayed on the chat box after pressing ENTER")
        self.util.sleep(sec=2)

    @pytest.mark.run(order=6)
    def test_logOut(self):
        """
        CHAT_008: Verify the user can log out of the chatroom successfully
        :return:
        """
        # Click account dropdown
        self.chatroom.clickAccountDropdown()
        result_dropdownOpen = self.chatroom.verifyAccountDropdownOpen()
        self.ts.mark(result_dropdownOpen, "Account dropdown opens after click")
        self.util.sleep(sec=1)

        # Click logout
        self.chatroom.clickLogOut()
        result_loginOpen = self.login.verifyLoginPageReached()
        self.ts.mark(result_loginOpen, "Logout is successful and the user reaches login page")
        self.util.sleep(sec=1)

        # Verify the success message is displayed
        result_messageDisplayed = self.login.verifyMessageDisplayed(state="logout")
        self.ts.mark(result_messageDisplayed, "Success message that indicate successful logout is displayed")
        self.util.sleep(sec=1)

        # Close the message
        self.login.clickCloseMessage()
        result_messageClosed = self.login.verifyMessageClosed(state="success")
        self.ts.markFinal("test_logOut", result_messageClosed, "The success message is closed successfully")
        self.util.sleep(sec=2)
