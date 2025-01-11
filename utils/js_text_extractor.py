from selenium.webdriver.remote.webelement import WebElement

def extract_text_via_js(element: WebElement) -> str:
    """
    Extracts and normalizes text content from an element using JavaScript.
    
    Args:
        element: The WebElement from which the text will be extracted.
    
    Returns:
        str: The normalized text content.
    """
    # Execute JavaScript to extract the text content
    text = element.parent.execute_script("return arguments[0].innerText;", element)
    
    # Normalize the text by joining any extra spaces into a single space
    return " ".join(text.split())
