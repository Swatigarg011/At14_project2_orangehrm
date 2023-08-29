import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from time import sleep

from Test_data import credentials

from Test_Locators.login_page_locators import LoginPageLocators
from Test_Locators.forgot_pass_page_locator import Forgot_Pass_PageLocator


class Test_Forget_Pass_LoginPageActions:

    @pytest.fixture
    def browser(self):
        self.loginlocators = LoginPageLocators()
        self.forgotpasslocator = Forgot_Pass_PageLocator()
        self.driver = webdriver.Chrome()
        self.driver.get(credentials.url)
        self.action = ActionChains(self.driver)
        self.wait = WebDriverWait(self.driver, 15)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        yield
        self.driver.close()

    def test_forgot_pass(self, browser):
        try:
            self.driver.get(credentials.url)

            forgot_pass = self.driver.find_element(By.XPATH, self.forgotpasslocator.forgot_password_locator)
            forgot_pass.click()
            sleep(3)

            username = self.driver.find_element(By.XPATH, self.forgotpasslocator.user_name_locator)
            username.send_keys(credentials.username)
            sleep(2)

            reset_pass = self.driver.find_element(By.XPATH, self.forgotpasslocator.reset_pass_button)
            reset_pass.click()
            sleep(3)

            print("Reset password link sent successfully")
        except NoSuchElementException:
            print('Element Missing')









