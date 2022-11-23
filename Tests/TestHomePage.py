from Config.Configdata import correct_number
from Locators.HomePageLocators import  you_pay
from Utilities.CommonPageUtilities import Util
from Utilities.HomePageUtilities import HomePageFunctions
from Utilities.LoginPageUtilities import *


@pytest.mark.usefixtures("initiate_driver")
class TestHomePage:

    def test_final_order(self):
        LoginPageFunctions().account_button()
        LoginPageFunctions().sign_in()
        LoginPageFunctions().perform_login(correct_number)
        HomePageFunctions().final_order()
        verify_text = Util().find(you_pay)
        assert verify_text.text == "You Pay"