import io
import os
import tempfile
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.js_text_extractor import extract_text_via_js
from utils.logger import log_with_timestamp
from utils.close_modal import close_modal
from utils.solve_captcha_osr_space import solve_captcha
from PIL import Image
from config.settings import OSR_SPACE_API_KEY


def make_appointment(driver, appointment_data):
    """
    Makes an appointment based on the user response.

    Args:
        driver: The WebDriver instance.
        appointment_data: The user response containing the session numbers.

    Returns:
        None
    """
    numbers_list = str(appointment_data).split(",")
    selected_sessions_by_day = {}
    for number in numbers_list:
        try:
            # close the modal
            close_modal(driver)
            # Wait for the page to refresh and the sessions to be available again
            WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "well")))
            available_sessions = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "well")))
            filtered_sessions = [session for session in available_sessions if session.value_of_css_property("border-color") == "rgb(8, 245, 26)"]
            
            session = filtered_sessions[int(number) - 1]
            session_button = session.find_element(By.XPATH, ".//span[4]/input")

            # Extract the session day from the panel heading
            session_day = extract_text_via_js(session.find_element(By.XPATH, "./ancestor::div[contains(@class, 'panel')]/div[contains(@class, 'panel-heading')]/h3[contains(@class, 'panel-title')]"))
            
            if session_day in selected_sessions_by_day:
                log_with_timestamp(f"Warning: A session for {session_day} has already been selected. Skipping session {number}")
                continue
            # Scroll the button into view (if necessary)
            driver.execute_script("arguments[0].scrollIntoView(true);", session_button)
            
            # Wait for the button to be clickable
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable(session_button))
            
            session_button.click()
            log_with_timestamp(f"Session {number} for {session_day} clicked successfully")

            # Track the selected session by day
            selected_sessions_by_day[session_day] = number
            
            # Wait for the page to refresh after clicking the button
            WebDriverWait(driver, 10).until(EC.staleness_of(session_button))
            
        except TimeoutException as e:
            log_with_timestamp(f"Error: TimeoutException occurred while processing session {number} - {str(e)}")
        except Exception as e:
            log_with_timestamp(f"Error: Exception occurred while processing session {number} - {str(e)}")

    appointment_checkbox = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "pageContent_cboxOnay")))
    appointment_submit = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "lbtnKaydet")))
    
    try:
        # close the modal
        close_modal(driver)
        appointment_checkbox.click()
        appointment_submit.click()
        log_with_timestamp("Appointment submitted successfully")
    except TimeoutException as e:
        log_with_timestamp(f"Error: TimeoutException occurred while submitting appointment - {str(e)}")
    except Exception as e:
        log_with_timestamp(f"Error: Exception occurred while submitting appointment - {str(e)}")
    
    
    # The following code was used to solve CAPTCHA, but the site has removed the CAPTCHA requirement.
    # Therefore, this code is no longer needed and has been commented out.

    # try:
    #     #close the modal
    #     close_modal(driver)

    #     captcha_element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "pageContent_captchaImage")))
    #     captcha_checkbox = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "pageContent_cboxOnay")))
    #     captcha_input = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "pageContent_txtCaptchaText")))
    #     final_button = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "lbtnKaydet")))

    #     screenshot = captcha_element.screenshot_as_png
    #     image = Image.open(io.BytesIO(screenshot))
        
    #     temp_dir = tempfile.gettempdir()

    #     image_path = os.path.join(temp_dir, "captcha.png")

    #     image.save(image_path)
    #     log_with_timestamp(f"Captcha image saved to: {image_path}")

    #     captcha_text = solve_captcha(image_path, OSR_SPACE_API_KEY)
    #     log_with_timestamp(f"Captcha text: {captcha_text}")

    #     captcha_checkbox.click()
    #     captcha_input.send_keys(captcha_text)
    #     final_button.click()

    #     # Delete the CAPTCHA image after extraction
    #     if os.path.exists(image_path):
    #         os.remove(image_path)
    #         print(f"Deleted CAPTCHA image: {image_path}")
    #     else:
    #         print(f"File not found: {image_path}")

    # except TimeoutException as e:
    #     log_with_timestamp(f"Error: TimeoutException occurred while locating captcha image - {str(e)}")
    # except Exception as e:
    #     log_with_timestamp(f"Error: Exception occurred while processing captcha image - {str(e)}")


    