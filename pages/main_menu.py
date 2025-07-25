from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page
from time import sleep

class MainMenu(Page):
    OFF_PLAN_MENU = (By.XPATH, "//div[@class='g-menu-text' and text()='Off-plan']")
    SECONDARY_MENU = (By.XPATH, "//button[text()='Secondary']")
    OFF_PLAN_AGAIN = (By.XPATH, "//a[@href='/off-plan' and text()='Off-plan']")




    #def go_to_secondary_then_off_plan(self):
        #sleep(5)
        #self.click(*self.SECONDARY_MENU)
        #sleep(5)
        #self.click(*self.OFF_PLAN_MENU)

    def go_to_off_plan(self, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        off_plan = wait.until(EC.element_to_be_clickable(self.OFF_PLAN_MENU))
        off_plan.click()

    def go_to_secondary(self, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        secondary = wait.until(EC.element_to_be_clickable(self.SECONDARY_MENU))
        secondary.click()

    def go_back_to_off_plan(self, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        off_plan_again = wait.until(EC.element_to_be_clickable(self.OFF_PLAN_AGAIN))
        off_plan_again.click()



