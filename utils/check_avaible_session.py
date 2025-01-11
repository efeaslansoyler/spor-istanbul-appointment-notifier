from selenium.webdriver.common.by import By
from utils.logger import log_with_timestamp
from utils.js_text_extractor import extract_text_via_js

def check_avaible_session(driver) -> str:
    log_with_timestamp("checking for available sessions")
    try:
        available_sessions = driver.find_elements(By.CLASS_NAME, "well")
        if not available_sessions:
            log_with_timestamp("No available sessions found")
            return "Uygun seans bulunamadı"
        log_with_timestamp(f"Found {len(available_sessions)} available sessions")
        message = ""
        for session in available_sessions:
            session_day = session.find_element(By.XPATH, "./ancestor::div[contains(@class, 'panel')]/div[contains(@class, 'panel-heading')]/h3[contains(@class, 'panel-title')]")
            session_time = session.find_element(By.XPATH, ".//span[2]")
            session_quota = session.find_element(By.XPATH, ".//span[3]")

            message += f"\n Seans günü: {extract_text_via_js(session_day)}, Seans Zamanı: {extract_text_via_js(session_time)}, Seans Kapasitesi: {extract_text_via_js(session_quota)}\n"
        return message
    except Exception as e:
        log_with_timestamp(f"Error checking for available sessions: {str(e)}")