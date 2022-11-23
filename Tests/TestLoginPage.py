from Config.Configdata import correct_number
from Locators.HomePageLocators import conformation_msg
from Utilities.LoginPageUtilities import *
from Utilities.CommonPageUtilities import *


@pytest.mark.usefixtures("initiate_driver")
class TestLoginPage:

    def test_verify_login_with_correct_mobile__num(self):
        LoginPageFunctions().account_button()
        LoginPageFunctions().sign_in()
        LoginPageFunctions().perform_login(correct_number)
        verify_text = Util().find(conformation_msg)
        assert verify_text.text == "You have successfully signed up! Enjoy the shopping at Nykaa Fashion", 'not working'
