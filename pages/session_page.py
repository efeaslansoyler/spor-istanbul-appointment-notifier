from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from utils.logger import log_with_timestamp

def check_session_availability(driver) -> None:
    log_with_timestamp("navigating to session page")
    driver.get("https://online.spor.istanbul/uyespor")

    try:
        log_with_timestamp("waiting for close modal button")
        close_modal_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Kapat']")))
        close_modal_button.click()
        log_with_timestamp("close modal button clicked")

        log_with_timestamp("waiting for modal backdrop to completely disappear")
        WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.CLASS_NAME, "modal-backdrop")))
        log_with_timestamp("modal backdrop disappeared")
        log_with_timestamp("session page reached successfully")
    except TimeoutException:
        log_with_timestamp("Warning: popup modal not found or not closed properly")

    try:
        log_with_timestamp("looking for session button")
        seans_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@class='btn btn-sm btn-success']")))
        seans_button.click()
        log_with_timestamp("Sessions page opened")
    except TimeoutException:
        log_with_timestamp("Error: Sessions button not found or not clickable")
        raise

    