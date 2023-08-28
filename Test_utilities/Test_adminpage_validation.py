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
from Test_Locators.admin_page_locator import AdminPageLocators


class Test_admin_PageActions:

    @pytest.fixture
    def browser(self):
        self.loginlocators = LoginPageLocators()
        self.forgotpasslocator = Forgot_Pass_PageLocator()
        self.adminpagelocator = AdminPageLocators()
        self.driver = webdriver.Chrome()
        self.driver.get(credentials.url)
        self.action = ActionChains(self.driver)
        self.wait = WebDriverWait(self.driver, 15)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        yield
        self.driver.close()

    def test_adminpage_validate(self, browser):
        try:
            self.driver.get(credentials.url)
            username = self.wait.until(EC.presence_of_element_located((By.NAME, self.loginlocators.username_locator)))
            # self.action.move_to_element(username.click(username).perform())
            username.send_keys(credentials.username)
            sleep(2)
            password = self.wait.until(EC.presence_of_element_located((By.NAME, self.loginlocators.password_locator)))
            password.send_keys(credentials.password)
            sleep(2)

            login_button = self.driver.find_element(By.XPATH,self.loginlocators.login_button_xpath)
            login_button.click()
            sleep(3)

            admin_tab = self.driver.find_element(By.XPATH,self.adminpagelocator.admin_tab_locator)
            admin_tab.click()
            sleep(3)

            user_manegment_tab = self.driver.find_element(By.XPATH,self.adminpagelocator.user_mange_tab_locator)
            self.action.move_to_element(user_manegment_tab).perform()
            if self.driver.find_element(By.XPATH,self.adminpagelocator.user_mange_tab_locator).is_displayed():
                print("User management element is validated")
            sleep(2)

            Job_tab = self.driver.find_element(By.XPATH, self.adminpagelocator.job_tab_locator)
            self.action.move_to_element(Job_tab).perform()
            if self.driver.find_element(By.XPATH,self.adminpagelocator.job_tab_locator).is_displayed():
                print("JOB element is validated")
            sleep(2)

            organization_tab = self.driver.find_element(By.XPATH, self.adminpagelocator.organization_tab_locator)
            self.action.move_to_element(organization_tab).perform()
            if self.driver.find_element(By.XPATH,self.adminpagelocator.organization_tab_locator).is_displayed():
                print("Organization Tab element is validated")
            sleep(2)

            Qualification_tab = self.driver.find_element(By.XPATH, self.adminpagelocator.Qualification_tab_locator)
            self.action.move_to_element(Qualification_tab).perform()
            if self.driver.find_element(By.XPATH, self.adminpagelocator.Qualification_tab_locator).is_displayed():
                print("Qualification Tab is validated")
            sleep(2)

            nationality_tab = self.driver.find_element(By.XPATH, self.adminpagelocator.nationality_tab_locator)
            self.action.move_to_element(nationality_tab).perform()
            if self.driver.find_element(By.XPATH, self.adminpagelocator.nationality_tab_locator).is_displayed():
                print("Nationality tab is validated")
            sleep(2)

            corp_branding_tab = self.driver.find_element(By.XPATH, self.adminpagelocator.corp_branding_tab_locator)
            self.action.move_to_element(corp_branding_tab).perform()
            if self.driver.find_element(By.XPATH, self.adminpagelocator.corp_branding_tab_locator).is_displayed():
                print("Corporating Branding Tab is validated")
            sleep(2)

            configuration_tab = self.driver.find_element(By.XPATH, self.adminpagelocator.configuration_tab_locator)
            self.action.move_to_element(configuration_tab).perform()
            if self.driver.find_element(By.XPATH, self.adminpagelocator.configuration_tab_locator).is_displayed():
                print("Configuration tab is validated")
            sleep(2)

            print("User is able to see all the admin page Header")



        except NoSuchElementException:
            print('Element Missing')











