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
from Test_Locators.menu_option_locator import MenuPageLocators
# from Test_Locators.admin_page_locator import AdminPageLocators


class Test_admin_Menu_PageActions:

    @pytest.fixture
    def browser(self):
        self.loginlocators = LoginPageLocators()
        self.adminpagemenu = MenuPageLocators()
        self.driver = webdriver.Chrome()
        self.driver.get(credentials.url)
        self.action = ActionChains(self.driver)
        self.wait = WebDriverWait(self.driver, 15)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        yield
        self.driver.close()

    def test_adminmenu_validate(self, browser):
        try:
            #launching to Orangehem website
            self.driver.get(credentials.url)
            # To check weather user is able to login
            username = self.wait.until(EC.presence_of_element_located((By.NAME, self.loginlocators.username_locator)))
            # self.action.move_to_element(username.click(username).perform())
            username.send_keys(credentials.username)
            sleep(2)
            password = self.wait.until(EC.presence_of_element_located((By.NAME, self.loginlocators.password_locator)))
            password.send_keys(credentials.password)
            sleep(2)

            login_button = self.driver.find_element(By.XPATH,self.loginlocators.login_button_xpath)
            login_button.click()
            sleep(2)

            # moving to Admin tab
            admin_tab = self.driver.find_element(By.XPATH, self.adminpagemenu.admin_tab_locator)
            admin_tab.click()
            if self.driver.find_element(By.XPATH, self.adminpagemenu.admin_tab_locator).is_displayed():
                print("Admin Tab element is validated")
            sleep(2)

            # moving to PIM tab
            PIM_tab = self.driver.find_element(By.XPATH, self.adminpagemenu.pim_tab_locator)
            self.action.move_to_element(PIM_tab).perform()
            if self.driver.find_element(By.XPATH, self.adminpagemenu.pim_tab_locator).is_displayed():
                print("PIM tab is validated")
            sleep(2)

            # moving to leave tab
            leave_tab = self.driver.find_element(By.XPATH, self.adminpagemenu.leave_tab_locator)
            self.action.move_to_element(leave_tab).perform()
            if self.driver.find_element(By.XPATH, self.adminpagemenu.leave_tab_locator).is_displayed():
                print("Leave tab is validated")
            sleep(2)

            # moving to time tab
            Time_tab = self.driver.find_element(By.XPATH, self.adminpagemenu.time_tab_locator)
            self.action.move_to_element(Time_tab).perform()
            if self.driver.find_element(By.XPATH, self.adminpagemenu.time_tab_locator).is_displayed():
                print("Time tab is validated")
            sleep(2)

            # moving to Recruitment tab
            recruitment_tab = self.driver.find_element(By.XPATH, self.adminpagemenu.recruitment_tab_locator)
            self.action.move_to_element(recruitment_tab).perform()
            if self.driver.find_element(By.XPATH, self.adminpagemenu.recruitment_tab_locator).is_displayed():
                print("Recruitment tab is validated")
            sleep(2)

            # moving to MY_INFO tab
            My_info_tab = self.driver.find_element(By.XPATH, self.adminpagemenu.my_info_tab_locator)
            self.action.move_to_element(My_info_tab).perform()
            if self.driver.find_element(By.XPATH, self.adminpagemenu.my_info_tab_locator).is_displayed():
                print("My_info tab is validated")
            sleep(2)

            # moving to Performance tab
            performance_tab = self.driver.find_element(By.XPATH, self.adminpagemenu.performance_tab_locator)
            self.action.move_to_element(performance_tab).perform()
            if self.driver.find_element(By.XPATH, self.adminpagemenu.performance_tab_locator).is_displayed():
                print("performance tab is validated")
                sleep(2)

            # moving to Dashboard tab
            dashboard_tab = self.driver.find_element(By.XPATH, self.adminpagemenu.dashboard_tab_locator)
            self.action.move_to_element(dashboard_tab).perform()
            if self.driver.find_element(By.XPATH, self.adminpagemenu.dashboard_tab_locator).is_displayed():
                print(" Dashboard tab is validated")
            sleep(2)

            # moving to Directory tab
            directory_tab = self.driver.find_element(By.XPATH, self.adminpagemenu.directory_tab_locator)
            self.action.move_to_element(directory_tab).perform()
            if self.driver.find_element(By.XPATH, self.adminpagemenu.directory_tab_locator).is_displayed():
                print("Directory tab is validated")
            sleep(2)

            # moving to Maintenance  tab
            maintenance_tab = self.driver.find_element(By.XPATH, self.adminpagemenu.maintence_tab_locator)
            self.action.move_to_element(maintenance_tab).perform()
            if self.driver.find_element(By.XPATH, self.adminpagemenu.maintence_tab_locator).is_displayed():
                print("Maintenance tab is validated")
                sleep(2)

            # moving to Claim tab
            claim_tab = self.driver.find_element(By.XPATH, self.adminpagemenu.claim_tab_locator)
            self.action.move_to_element(claim_tab).perform()
            if self.driver.find_element(By.XPATH, self.adminpagemenu.claim_tab_locator).is_displayed():
                print("Claim tab is validated")
            sleep(2)

            # moving to Buzz tab
            buzz_tab = self.driver.find_element(By.XPATH, self.adminpagemenu.buzz_tab_locator)
            self.action.move_to_element(buzz_tab).perform()
            if self.driver.find_element(By.XPATH, self.adminpagemenu.buzz_tab_locator).is_displayed():
                print("Buzz tab is validated")
            sleep(2)
            print("user is able to see Admin page menu item")

        except NoSuchElementException:
            print('Element Missing')

