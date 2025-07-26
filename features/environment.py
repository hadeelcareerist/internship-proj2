from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
from app.application import Application
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support.ui import WebDriverWait

def browser_init(context):
    """

    :param context: Behave context
    """
    # username = 'hadeelaltameemi_DKs0be'
    # access_key = 'jvAs1VKy5VjMLwZa2BLD'
    # options = Options()
    # options.set_capability('browserName', 'Chrome')
    # options.set_capability('browserVersion', 'latest')
    # options.set_capability('bstack:options', {
    #     'os': 'Windows',
    #     'osVersion': '10',
    #     'projectName': 'Reelly POM Tests',
    #     'buildName' : 'Reelly POM Tests',
    #     'sessionName': 'Behave Test Session',
    #     'debug': True,
    #     'networkLogs': True,
    #     'seleniumVersion':'4.0.0',
    #     })
    # hub_url = f'http://{username}:{access_key}@hub-cloud.browserstack.com/wd/hub'










    ### Chrome ####
    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service)
    # context.driver.maximize_window()

    ## Headless Mode ####
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    service = Service(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(
        options=options,
        service=service
     )
    context.driver.set_window_size(1920, 1080)

    ### Firefox ####
    # driver_path = GeckoDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Firefox(service=service)
    #
    # context.driver = webdriver.Remote(command_executor=hub_url, options=options)
    # context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 30)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()