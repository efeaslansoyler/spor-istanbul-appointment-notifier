from utils.send_sms import send_sms
from utils.driver import create_firefox_driver
from utils.check_avaible_session import check_avaible_session
from pages.login_page import login
from pages.session_page import session_page
from config.settings import users

def notify_users(user: dict, message: str):
    phone_number = user['phone_number']
    if phone_number:
        send_sms(phone_number, message)

def check_session_and_notify() -> None:
    for user in users:
        username = user['username']
        password = user['password']

        driver = create_firefox_driver()

        login(driver, username, password)

        session_page(driver)

        message = check_avaible_session(driver)


        notify_users(user,message)
        
        driver.quit()

if __name__ == "__main__":
    check_session_and_notify()
    print("done")