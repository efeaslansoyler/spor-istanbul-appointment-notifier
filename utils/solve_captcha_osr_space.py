import requests
def solve_captcha(image_path, api_key):
    url = "https://api.ocr.space/parse/image"
    with open(image_path, "rb") as image_file:
        response = requests.post(
            url,
            files={"file": image_file},
            data={"apikey": api_key, "language": "eng", "OCREngine": 2}
        )
    result = response.json()
    if result["IsErroredOnProcessing"]:
        print("Error:", result["ErrorMessage"])
        return None
    captcha_text = result["ParsedResults"][0]["ParsedText"].strip()
    return captcha_text
