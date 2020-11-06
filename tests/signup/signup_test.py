from pages.signup_page import SignupPage
from utilities.teststatus import TestStatus
import unittest
import pytest
import utilities.util as util
from random import randint

@pytest.mark.usefixtures("oneTimeSetup", "setUp")
class SignupTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetup):
        self.signup = SignupPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.util = util.Util()

    @pytest.mark.run(order=1)
    def test_navigateSignupPage(self):
        """
        SIGNUP_009: Verify successful navigation to sign up page
        :return:
        """
        self.signup.navigateToSignup()
        result_navigateToSignup = self.signup.verifySignupReached()
        self.ts.markFinal("test_navigateSignupPage", result_navigateToSignup, "Successfully navigate to the Sign Up page")
        self.util.sleep(sec=2)

    @pytest.mark.run(order=2)
    def test_createExistingAccount(self):
        """
        SIGNUP_001: Verify signing up with an existing account will trigger an error message
        :return:
        """
        username = "test1"
        password = "testpassword"

        # Verify error message is displayed
        self.signup.creatingAccount(username, password=password, password_confirmation=password)
        result_signupFail = self.signup.verifyMessageDisplayed("error")
        self.ts.mark(result_signupFail, "As expected: an user can't create an existing account")
        self.util.sleep(sec=1)

        # Verify error message is closed
        self.signup.clickCloseMessage()
        result_closeMessage = self.signup.verifyMessageClosed("error")
        self.ts.markFinal("test_createExistingAccount", result_closeMessage, "The error message is closed successfully")

        self.signup.cleanUpUsernameAndPassword()
        self.util.sleep(sec=2)

    @pytest.mark.run(order=3)
    def test_signupAllEmpty(self):
        """
        SIGNUP_002: Verify signing up with an empty username and password triggers an error message
        :return:
        """
        # Verify error message is displayed
        self.signup.clickSignupSubmit()
        result_signupEmpty = self.signup.verifyMessageDisplayed("error")
        self.ts.mark(result_signupEmpty, "As expected: an user can't signup with empty username and password")
        self.util.sleep(sec=1)

        # Verify error message is closed
        self.signup.clickCloseMessage()
        result_closeMessage = self.signup.verifyMessageClosed("error")
        self.ts.markFinal("test_signupAllEmpty", result_closeMessage, "The error message is closed successfully")

        self.signup.cleanUpUsernameAndPassword()
        self.util.sleep(sec=2)

    @pytest.mark.run(order=4)
    def test_signupOneEmpty(self):
        """
        SIGNUP_003: Verify signing up with an empy username or password triggers an error message
        :return:
        """
        username = ""
        password = "testpassword"
        self.signup.creatingAccount(username, password=password, password_confirmation=password)

        # Verify error message is displayed
        result_signupFail = self.signup.verifyMessageDisplayed("error")
        self.ts.mark(result_signupFail, "As expected: an user can't signup with empty username")
        self.util.sleep(sec=1)

        # Verify error message is closed
        self.signup.clickCloseMessage()
        result_closeMessage = self.signup.verifyMessageClosed("error")
        self.ts.mark(result_closeMessage, "The error message is closed successfully")
        self.signup.cleanUpUsernameAndPassword()
        self.util.sleep(sec=1)

        username = "test1"
        password = ""

        # Verify error message is displayed
        self.signup.creatingAccount(username, password=password, password_confirmation=password)
        result_signupFail = self.signup.verifyMessageDisplayed("error")
        self.ts.mark(result_signupFail, "As expected: an user can't signup with empty password")
        self.util.sleep(sec=1)

        # Verify error message is closed
        self.signup.clickCloseMessage()
        result_closeMessage = self.signup.verifyMessageClosed("error")
        self.ts.markFinal("test_signupOneEmpty", result_closeMessage, "The error message is closed successfully")
        self.signup.cleanUpUsernameAndPassword()
        self.util.sleep(sec=2)

    @pytest.mark.run(order=5)
    def test_signupFalseConfirmationPassword(self):
        """
        SIGNUP_004: Verify signing up with a confirmation password that is different from the password
        :return:
        """
        username = "test1"
        password = "testpassword1"
        passwordConfirmation = "testpassword2"

        # Verify error message is displayed
        self.signup.creatingAccount(username, password=password, password_confirmation=passwordConfirmation)
        result_signupFail = self.signup.verifyMessageDisplayed("error")
        self.ts.mark(result_signupFail, "As expected: an user can't signup with false password confirmation")
        self.util.sleep(sec=1)

        # Verify error message is closed
        self.signup.clickCloseMessage()
        result_closeMessage = self.signup.verifyMessageClosed("error")
        self.ts.markFinal("test_signupFalseConfirmation", result_closeMessage,
                          "The error message is closed successfully")

        self.signup.cleanUpUsernameAndPassword()
        self.util.sleep(sec=2)

    @pytest.mark.run(order=6)
    def test_signupSuccess(self):
        """
        SIGNUP_005: Verify signing up with a confirmation password that is different from the password
        :return:
        """
        username = "test" + str(randint(0,10000000000))
        password = "test" + str(randint(0,10000000000))
        self.util.sleep(sec=1)

        # Verify success message is displayed
        self.signup.creatingAccount(username, password=password, password_confirmation=password)
        result_returnHome = self.signup.verifyNavigateHome()
        result_signupSuccess = self.signup.verifyMessageDisplayed("success", username)
        self.ts.mark((result_signupSuccess and result_returnHome), "User successfully creates an account")
        self.util.sleep(sec=1)

        # Verify error message is closed
        self.signup.clickCloseMessage()
        result_closeMessage = self.signup.verifyMessageClosed("success")
        self.ts.markFinal("test_signupFalseConfirmation", result_closeMessage,
                          "The error message is closed successfully")
        self.util.sleep(sec=2)

    @pytest.mark.run(order=7)
    def test_returnHome(self):
        """
        SIGNUP_006: Verify clicking cancel in the sign up page will return to the home page
        :return:
        """
        self.signup.navigateToSignup()
        self.util.sleep(sec=1)

        # Verify the user returns to home page
        self.signup.clickReturnHome()
        result_returnHome = self.signup.verifyNavigateHome()
        self.ts.markFinal("test_signupSuccess", result_returnHome, "Successfully return to the home page")
        self.util.sleep(sec=2)

    @pytest.mark.run(order=8)
    def test_useLoginNavigationLinks(self):
        """
        SIGNUP_007: Verify clicking "Log In" Navigation Link on the Sign Up Page will open the Login Page
        :return:
        """
        self.signup.navigateToSignup()
        self.util.sleep(sec=1)

        # Verify the user navigates to the home page
        self.signup.clickLoginNavigation()
        result_returnHome = self.signup.verifyNavigateHome()
        self.ts.mark(result_returnHome, "Successfully return to login page by using login navigation link")

        self.signup.navigateToSignup()
        self.util.sleep(sec=1)

        # Verify clicking account dropdown opens the dropdown menu
        self.signup.clickAccountDropdown()
        result_dropdownVisible = self.signup.verifyDropdownVisible()
        self.ts.mark(result_dropdownVisible, "Account dropdown menu is visible after click")

        # Verify the user navigates to the home page
        self.signup.clickLoginUnderDropdown()
        result_returnHome = self.signup.verifyNavigateHome()
        self.ts.markFinal("test_useLoginNavigationLinks", result_returnHome,
                          "Successfully return to login page by using login link under account dropdown")
        self.util.sleep(sec=2)

    @pytest.mark.run(order=9)
    def test_useChatroomLink(self):
        """
        SIGNUP_008: Verify clicking "Chatroom" Navigation Link on the Sign Up Page will open the Login Page
        :return:
        """
        self.signup.navigateToSignup()
        self.util.sleep(sec=1)

        # Verify successful return to home page
        self.signup.clickChatroomLink()
        result_returnHome = self.signup.verifyNavigateHome()
        self.ts.mark(result_returnHome, "Successfully return to login page when the user is not logged in")

        # Verify error message is displayed
        result_messagePresent = self.signup.verifyMessageDisplayed(state="chatroomError")
        self.ts.markFinal("test_useChatroomLink", result_messagePresent,
                          "Error message shows up because the user is not logged in")
        self.util.sleep(sec=2)

    @pytest.mark.run(order=10)
    def test_useMessagesLink(self):
        """
        SIGNUP_008: Verify clicking "Messages" Navigation Link on the Sign Up Page will open the Login Page
        :return:
        """
        self.signup.navigateToSignup()
        self.util.sleep(sec=1)

        # Verify successful return to home page
        self.signup.clickMessagesLink()
        result_returnHome = self.signup.verifyNavigateHome()
        self.ts.mark(result_returnHome, "Successfully return to login page when the user is not logged in")

        # Verify error message is displayed
        result_messagePresent = self.signup.verifyMessageDisplayed(state="messagesError")
        self.ts.markFinal("test_useMessagesLink", result_messagePresent,
                          "Error message shows up because the user is not logged in")
        self.util.sleep(sec=2)


