from pages.login_page import LoginPage
from utilities.teststatus import TestStatus
import unittest
import pytest
import utilities.util as util

@pytest.mark.usefixtures("oneTimeSetup", "setUp")
class SignupTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetup):
        self.login = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.util = util.Util()

    @pytest.mark.run(order=1)
    def test_useLoginNavigation(self):
        """
        LOGIN_001: Verify clicking log in navigation link on the Login Page will open the login page
        :return:
        """
        # Verify successfully navigates to the login page
        self.login.clickLoginNavigation()
        result_navigateLogin = self.login.verifyLoginPageReached()
        self.ts.mark(result_navigateLogin, "Successfully return to login page by using login navigation link")
        self.util.sleep(sec=1)

        # Verify the dropdown is visble
        self.login.clickAccountDropdown()
        result_dropdownVisible = self.login.verifyDropdownVisible()
        self.ts.mark(result_dropdownVisible, "The dropdown menu is visible after click")

        # Verify successfully navigates to the login page
        self.login.clickLoginUnderDropdown()
        result_navigateLogin = self.login.verifyLoginPageReached()
        self.ts.markFinal("test_useLoginNavigation", result_navigateLogin,
                          "Successfully return to login page by using login link under account dropdown")
        self.util.sleep(sec=2)

    @pytest.mark.run(order=2)
    def test_useChatroomLink(self):
        """
        LOGIN_002: Verify clicking "Chatroom" when the user is not logged in will open the login page
        :return:
        """
        # Verify successful return to home page
        self.login.clickChatroomLink()
        result_returnHome = self.login.verifyLoginPageReached()
        self.ts.mark(result_returnHome, "Return to login page after clicking 'Chatroom' when the user is not logged in")

        # Verify error message is displayed
        result_messagePresent = self.login.verifyMessageDisplayed(state="chatroomError")
        self.ts.markFinal("test_useChatroomLink", result_messagePresent,
                          "Error message shows up because the user is not logged in")
        self.util.sleep(sec=2)

    @pytest.mark.run(order=3)
    def test_useMessagesLink(self):
        """
        LOGIN_002: Verify clicking "Messages" when the user is not logged in will open the login page
        :return:
        """
        # Verify successful return to home page
        self.login.clickMessagesLink()
        result_returnHome = self.login.verifyLoginPageReached()
        self.ts.mark(result_returnHome, "Return to login page after clicking 'Messages' when the user is not logged in")

        # Verify error message is displayed
        result_messagePresent = self.login.verifyMessageDisplayed(state="messagesError")
        self.ts.markFinal("test_useMessagesLink", result_messagePresent,
                          "Error message shows up because the user is not logged in")
        self.util.sleep(sec=2)

    @pytest.mark.run(order=4)
    def test_loginAllEmpty(self):
        """
        LOGIN_003: Verify login with empty username and password triggers an error message
        :return:
        """
        # Verify error message is displayed
        self.login.clickLoginSubmit()
        result_signupEmpty = self.login.verifyMessageDisplayed("error")
        self.ts.mark(result_signupEmpty, "As expected: an user can't login with empty username and password")
        self.util.sleep(sec=1)

        # Verify error message is closed
        self.login.clickCloseMessage()
        result_closeMessage = self.login.verifyMessageClosed("error")
        self.ts.markFinal("test_loginAllEmpty", result_closeMessage, "The error message is closed successfully")

    @pytest.mark.run(order=5)
    def test_loginOneEmpty(self):
        """
        LOGIN_004: Verify login with an empty username or an empty password triggers an error message
        :return:
        """
        username = ""
        password = "testpassword1"
        self.login.loggingAccount(username, password)

        # Verify error message is displayed
        result_signupFail = self.login.verifyMessageDisplayed("error")
        self.ts.mark(result_signupFail, "As expected: an user can't login with empty username")
        self.util.sleep(sec=1)

        # Verify error message is closed
        self.login.clickCloseMessage()
        result_closeMessage = self.login.verifyMessageClosed("error")
        self.ts.mark(result_closeMessage, "The error message is closed successfully")
        self.util.sleep(sec=1)

        username = "test1"
        password = ""

        # Verify error message is displayed
        self.login.loggingAccount(username, password)
        result_loginFail = self.login.verifyMessageDisplayed("error")
        self.ts.mark(result_loginFail, "As expected: an user can't login with empty password")
        self.util.sleep(sec=1)

        # Verify error message is closed
        self.login.clickCloseMessage()
        result_closeMessage = self.login.verifyMessageClosed("error")
        self.ts.markFinal("test_loginOneEmpty", result_closeMessage, "The error message is closed successfully")
        self.util.sleep(sec=2)

    @pytest.mark.run(order=6)
    def test_createNonExistentAccount(self):
        """
        LOGIN_005: Verify login with a non-existent account triggers an error message
        :return:
        """
        username = "FalseTest"
        password = "FalsePassword"

        # Verify error message is displayed
        self.login.loggingAccount(username, password)
        result_loginFail = self.login.verifyMessageDisplayed("error")
        self.ts.mark(result_loginFail, "As expected: an user can't login to a non-existent account")
        self.util.sleep(sec=1)

        # Verify error message is closed
        self.login.clickCloseMessage()
        result_closeMessage = self.login.verifyMessageClosed("error")
        self.ts.markFinal("test_createNonExistentAccount", result_closeMessage,
                          "The error message is closed successfully")
        self.util.sleep(sec=2)

    @pytest.mark.run(order=7)
    def test_loginWrongPassword(self):
        """
        LOGIN_006: Verify login with a wrong password triggers an error message
        :return:
        """
        username = "test1"
        password = "FalsePassword"

        # Verify error message is displayed
        self.login.loggingAccount(username, password)
        result_loginFail = self.login.verifyMessageDisplayed("error")
        self.ts.mark(result_loginFail, "As expected: an user can't login with a wrong password")
        self.util.sleep(sec=1)

        # Verify error message is close
        self.login.clickCloseMessage()
        result_closeMessage = self.login.verifyMessageClosed("error")
        self.ts.markFinal("test_loginWrongPassword", result_closeMessage, "The error message is closed successfully")
        self.util.sleep(sec=2)

    @pytest.mark.run(order=8)
    def test_successfulLogin(self):
        """
        LOGIN_007: Verify login with a correct username and password navigates the user to the chatroom
        :return:
        """
        username = "test1"
        password = "testpassword"

        # Verify successful login
        self.login.loggingAccount(username, password)
        result_loginSuccess = self.login.verifyNavigateChatroom()
        self.ts.mark(result_loginSuccess, "The user successfully navigates to the chatroom page")

        # Verify success message is displayed
        result_successMessage = self.login.verifyMessageDisplayed(state="success")
        self.ts.mark(result_successMessage, "The success message is displayed")
        self.util.sleep(sec=1)

        # Verify success message is closed
        self.login.clickCloseMessage()
        result_closeMessage = self.login.verifyMessageClosed("success")
        self.ts.markFinal("test_successfulLogin", result_closeMessage, "The success message is closed successfully")
        self.util.sleep(sec=2)

