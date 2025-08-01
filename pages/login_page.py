from time import sleep
from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.common.action_chains import ActionChains


class LoginPage(Page):

    EMAIL = (By.CSS_SELECTOR, "input[type='email']")
    PASSWORD = (By.CSS_SELECTOR, "input[type='password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "a[wized='loginButton']")

    def open_login_page(self):
        self.open_url('https://soft.reelly.io/sign-in')

    def login(self, email, password):
        # sleep(5)
        self.input_text(email, *self.EMAIL)
        self.input_text(password, *self.PASSWORD)
        actions = ActionChains(self.driver)
        actions.move_by_offset(0, 0).click().perform()
        self.click(*self.LOGIN_BUTTON)
