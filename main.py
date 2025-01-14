import time
import threading

from utils.driver import create_firefox_driver
from utils.logger import log_with_timestamp
from utils.send_sms import send_sms
from utils.check_available_session import check_available_session
from utils.receive_sms import get_latest_message, start_flask_app

from config.settings import users, MAX_RETRIES, RETRY_DELAY
from pages.login_page import login
from pages.session_page import session_page

def check_session_and_notify() -> None:
    """
    Checks session availability for each user and sends an SMS notification if available.
    Retries the process if it fails, up to MAX_RETRIES times.
    """
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

                # Create a new Firefox driver instance
                driver = create_firefox_driver()

                # Log in to the website
                login(driver, username, password)

                # Navigate to the session page
                session_page(driver)
                
                # Check for available sessions
                message = check_available_session(driver)

                # Send an SMS notification with the session details
                send_sms(user_phone_number, message)

                #Wait for user response
                log_with_timestamp(f"Waiting for user response for user: {username}")
                time.sleep(60)

                appointment_data = get_latest_message()
                if appointment_data:
                    log_with_timestamp(f"User response received for user: {username} - {appointment_data}")
                else:
                    log_with_timestamp(f"No response received for user: {username}")

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
    flask_thread = threading.Thread(target=start_flask_app)
    flask_thread.daemon = True
    flask_thread.start()
    check_session_and_notify()