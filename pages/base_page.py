from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class Page:

    def __init__(self, driver):
        self.driver = driver #attribute driver inside the class page
        self.wait = WebDriverWait(driver, 10)

#page = Page("driver")
#print(page.driver)
    def open_url(self, url):
        self.driver.get(url)

    def find_element(self, *locator):
       return self.driver.find_element(*locator)
    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def click(self, *locator):
        self.wait.until(EC.element_to_be_clickable(locator), message=f'Element by {locator} not clickable').click()


    def input_text(self, text,  *locator):
        self.wait.until(EC.presence_of_element_located(locator)).send_keys(text)


