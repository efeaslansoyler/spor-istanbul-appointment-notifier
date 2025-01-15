from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import log_with_timestamp
from utils.js_text_extractor import extract_text_via_js

def check_available_session(driver) -> str:
    """
    Checks for available sessions on the website and returns the session details.

    Args:
        driver: The WebDriver instance.

    Returns:
        str: A message containing the session details.
    """
    log_with_timestamp("Checking for available sessions")
    try:
        available_sessions = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "well")))
        filtered_sessions = [
            session for session in available_sessions if session.value_of_css_property("border-color") == "rgb(8, 245, 26)"
        ]
        message = ""
        i = 1
        if not filtered_sessions:
            log_with_timestamp("No available sessions found")
            message += "Uygun seans bulunamadı"
            return message
        log_with_timestamp(f"Found {len(filtered_sessions)} available sessions")
        for session in filtered_sessions:
            session_day = session.find_element(By.XPATH, "./ancestor::div[contains(@class, 'panel')]/div[contains(@class, 'panel-heading')]/h3[contains(@class, 'panel-title')]")
            session_time = session.find_element(By.XPATH, ".//span[2]")
            session_quota = session.find_element(By.XPATH, ".//span[3]")

            message += f"\n {[i]} - Seans günü: {extract_text_via_js(session_day)}, Seans Zamanı: {extract_text_via_js(session_time)}, Seans Kapasitesi: {extract_text_via_js(session_quota)}\n"
            i += 1
        message += f"\n Lütfen istediğiniz seansın numarasını giriniz. Birden fazla seans almak için numaraları virgülle ayırabilirsiniz. Örnek: 1,2,3. Cevabınızı en geç 2 dakika içinde vermeniz gerekecektir. Aynı günden sadece 1 tane seans seçebilirsiniz."
        return message
    except Exception as e:
        log_with_timestamp(f"Error checking for available sessions: {str(e)}")