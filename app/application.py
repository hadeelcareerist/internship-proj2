from pages.base_page import Page
from pages.login_page import LoginPage
from pages.main_menu import MainMenu
from pages.off_plan_page import OffPlanPage

class Application:
    def __init__(self, driver):
        self.driver = driver
        self.base_page = Page(self.driver)
        self.login_page = LoginPage(driver)
        self.menu = MainMenu(driver)
        self.off_plan = OffPlanPage(driver)

