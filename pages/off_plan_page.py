from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class OffPlanPage(Page):
    OFF_PLAN_BUTTON = (By.XPATH, "//div[contains(@class, 'menu-text') and contains(text(), 'Off-plan')]")
    NEXT_PAGE_BUTTON = (By.XPATH, "//*[contains(text(), 'Next page')]")
    PREV_PAGE_BUTTON = (By.XPATH, "//div[normalize-space()='Previous page']")

    def verify_off_plan_page(self):
        assert self.find_element(*self.OFF_PLAN_BUTTON).is_displayed(), "Off-plan button not visible"

    def go_to_final_page(self):
        next_button = (By.CSS_SELECTOR, "button[aria-label='Go to next page']")

        while True:
            try:
                next_btn = self.find_element(*self.NEXT_PAGE_BUTTON)
                if not next_btn.is_enabled() or 'disabled' in next_btn.get_attribute('class'):
                    print("Reached last page.")
                    break
                self.click(*self.NEXT_PAGE_BUTTON)
            except:
                break


    def go_to_first_page(self):
        while True:
            try:
                self.click(*self.PREV_PAGE_BUTTON)
            except:
                print("Reached the first page")
                break
