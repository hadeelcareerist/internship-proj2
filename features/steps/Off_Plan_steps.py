from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then

@given('I open the Reelly site')
def step_open_website(context):
    context.driver = webdriver.Chrome()
    context.driver.get('https://soft.reelly.io/sign-in')
    context.driver.maximize_window()


@when ('I log in')
def step_login(context):
    wait = WebDriverWait(context.driver, 10)
    email_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='email']")))
    email_input.send_keys("hadeel.altameemi@gmail.com")

    password_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='password']")))
    password_input.send_keys("Hadoola@2hm")

    sign_in_btn = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "a[wized='loginButton']")))
    sign_in_btn.click()



@when('I click on the off plan menu')
def step_click_off_plan(context):
    wait=WebDriverWait(context.driver, 20)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'menu-text') and contains(normalize-space(.), 'Off-plan')]")
    )).click()

@then("I should be on the off plan page")
def step_verify_off_plan_page(context):
    wait = WebDriverWait(context.driver, 15)
    off_plan_btn = wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(@class, 'pb-5') and contains(text(), 'Off-plan')]")))
    assert off_plan_btn.is_displayed(), "Off-plan button is not visible, not on the off plan page"
@when("I go to the final page using the pagination button")
def step_go_to_final_page(context):
    wait = WebDriverWait(context.driver, 10)
    while True:
        try:
         next_button = wait.until( EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Next page')]"))).click()
        except:
            print("Reached the last page")
        break

@when("I go back to the first page using the pagination button")
def step_go_to_first_page(context):
    wait = WebDriverWait(context.driver, 10)
    while True:
       try:
         prev_button= wait.until(EC.element_to_be_clickable(By.XPATH, "//div[normalize-space()='Previous page']"))
         prev_button.click()
       except:
           print("Reached to the first page")
       break



@then("I close the browser")
def step_close_browser(context):
    context.driver.quit()
