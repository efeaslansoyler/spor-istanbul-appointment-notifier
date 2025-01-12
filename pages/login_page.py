from selenium.webdriver.common.by import By
from utils.logger import log_with_timestamp

def login(driver, username: str, password: str) -> None:
    """
    Logs in to the website using the provided username and password.

    Args:
        driver: The WebDriver instance.
        username (str): The username for login.
        password (str): The password for login.
    """
    try:
        log_with_timestamp("Navigating to login page")
        driver.get("https://online.spor.istanbul/uyegiris")
        
        log_with_timestamp("Login page reached successfully")
        username_field = driver.find_element(By.ID, "txtTCPasaport")
        password_field = driver.find_element(By.ID, "txtSifre")
        login_button = driver.find_element(By.ID, "btnGirisYap")

        log_with_timestamp("Filling in username and password")
        username_field.send_keys(username)
        password_field.send_keys(password)
        login_button.click()
        if "anasayfa" not in driver.current_url:
            log_with_timestamp("Login failed")
            raise Exception("Login failed")
        log_with_timestamp("Login successful")
    except Exception as e:
        log_with_timestamp(f"Failed to navigate to login page: {str(e)}")
        raise e