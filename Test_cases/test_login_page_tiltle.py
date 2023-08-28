from Test_utilities.Test_forgot_pass_login import LoginPageActions


class TestLoginTitle:

    def __init__(self):
        pass

    def test_login_page_title(self):
        """
        test case to test the title of our webpage
        :return:
        """
        _expected_title = "OrangeHRM"

        LoginPageActions().login_to_orangehrm()
        assert LoginPageActions().title_of_page() == _expected_title


TestLoginTitle().test_login_page_title()
