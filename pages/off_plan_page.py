from time import sleep

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException


class OffPlanPage(Page):
    OFF_PLAN_BUTTON = (By.XPATH, "//div[contains(@class, 'menu-text') and contains(text(), 'Off-plan')]")
    OFF_PLAN_BUTTON_MOBILE = (By.XPATH, "//a[@href='/off-plan' and contains(@class, 'menu-text-link-leaderboard')]")

    NEXT_PAGE_BUTTON = (By.XPATH, "//*[contains(text(), 'Next page')]")
    NEXT_PAGE_BUTTON_MOBILE = (By.XPATH, "//a[contains(@class, 'pagination__button') and ./div[text()='Next page']]")

    PREV_PAGE_BUTTON = (By.CSS_SELECTOR, '[wized="previousPageProperties"]')
    PREV_PAGE_BUTTON_MOBILE = (By.XPATH, "//div[contains(@class, 'pagination__button')]//div[text()='Prev. page']")


    def verify_off_plan_page(self):
        assert self.find_element(*self.OFF_PLAN_BUTTON).is_displayed(), "Off-plan button not visible"

    def verify_off_plan_page_mobile(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(self.OFF_PLAN_BUTTON_MOBILE))






    def go_to_final_page(self):
        next_button = (By.CSS_SELECTOR, "button[aria-label='Go to next page']")

        total_page = 2
        for btn in range(0, total_page+1):
            sleep(3)
            self.click(*self.NEXT_PAGE_BUTTON)

    def go_to_final_page_mobile(self):
        self.NEXT_PAGE_BUTTON_MOBILE= (By.XPATH, "//a[contains(@class, 'pagination__button') and ./div[text()='Next page']]")

        total_page = 2
        for btn in range(0, total_page+1):
            sleep(3)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            self.click(*self.NEXT_PAGE_BUTTON_MOBILE)

        # while True:
        #     try:
        #         next_btn = self.find_element(*self.NEXT_PAGE_BUTTON)
        #         if not next_btn.is_enabled() or 'disabled' in next_btn.get_attribute('class'):
        #             print("Reached last page.")
        #             break
        #         self.click(*self.NEXT_PAGE_BUTTON)
        #     except:
        #         break


    def go_to_first_page(self):
        # while True:
        #     try:
        #         self.click(*self.PREV_PAGE_BUTTON)
        #     except:
        #         print("Reached the first page")
        #         break
        total_page = 2
        for btn in range(0, total_page + 1):
            sleep(5)
            self.click(*self.PREV_PAGE_BUTTON)

    def go_to_first_page_mobile(self):
        total_page = 2
        for btn in range(0, total_page + 1):
            sleep(5)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            self.click(*self.PREV_PAGE_BUTTON_MOBILE)
