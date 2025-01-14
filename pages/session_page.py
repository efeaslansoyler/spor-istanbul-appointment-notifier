from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from utils.logger import log_with_timestamp
from utils.close_modal import close_modal

def session_page(driver) -> None:
    """
    Navigates to the session page and handles any pop-up modals.

    Args:
        driver: The WebDriver instance.
    """
    log_with_timestamp("Navigating to session page")
    driver.get("https://online.spor.istanbul/uyespor")

    # Close the modal if it appears
    close_modal(driver)

    try:
        log_with_timestamp("Looking for session button")
        seans_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@class='btn btn-sm btn-success']")))
        seans_button.click()
        log_with_timestamp("Sessions page opened")
    except TimeoutException:
        log_with_timestamp("Error: Sessions button not found or not clickable")
        raise