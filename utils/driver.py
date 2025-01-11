from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from utils.logger import log_with_timestamp

def create_firefox_driver() -> webdriver.Firefox:
    """
    Creates and returns a headless Firefox WebDriver.
    
    Returns:
        A headless Firefox WebDriver instance.
    """
    try:
        log_with_timestamp("Creating Firefox driver")
        options = Options()
        options.headless = True
        driver = webdriver.Firefox(options=options)
        log_with_timestamp("Firefox driver created successfully")
        return driver
    except Exception as e:
        log_with_timestamp(f"Failed to create Firefox driver: {str(e)}")
        raise e