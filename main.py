import time

from utils.driver import create_firefox_driver
from utils.logger import log_with_timestamp
from utils.send_sms import send_sms
from utils.check_available_session import check_available_session

from config.settings import users, MAX_RETRIES, RETRY_DELAY
from pages.login_page import login
from pages.session_page import session_page

def check_session_and_notify() -> None:
    for user in users:
        username = user['username']
        password = user['password']
        user_phone_number = user['phone_number']

        retry_count = 0
        success = False
        driver = None

        while retry_count < MAX_RETRIES and not success:
            try:
                retry_count += 1
                log_with_timestamp(f"User: {username} - Attempt {retry_count}/{MAX_RETRIES} to check session availability")

                driver = create_firefox_driver()

                login(driver, username, password)

                session_page(driver)
                
                message = check_available_session(driver)

                send_sms(user_phone_number, message)

                log_with_timestamp(f"Session check for {username} completed successfully")
                success = True
            except Exception as e:
                log_with_timestamp(f"Error for user {username} on attempt {retry_count}/{MAX_RETRIES}: {e}")

                if retry_count < MAX_RETRIES:
                    log_with_timestamp(f"Waiting for {RETRY_DELAY} seconds before retrying for user: {username}")
                    time.sleep(RETRY_DELAY)

            finally:
                if driver:
                    driver.quit()

if __name__ == "__main__":
    check_session_and_notify()