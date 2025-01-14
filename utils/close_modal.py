from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import log_with_timestamp
from selenium.common.exceptions import TimeoutException

def close_modal(driver):
    try:
        log_with_timestamp("Waiting for close modal button")
        close_modal_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Kapat']")))
        close_modal_button.click()
        log_with_timestamp("Close modal button clicked")

        log_with_timestamp("Waiting for modal backdrop to completely disappear")
        WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.CLASS_NAME, "modal-backdrop")))
        log_with_timestamp("Modal backdrop disappeared")
        log_with_timestamp("Session page reached successfully")
    except TimeoutException:
        log_with_timestamp("Warning: Popup modal not found or not closed properly")