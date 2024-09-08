import pyautogui
import time

def wait_for_image(image_path, confidence=0.7, delay=7):
    while True:
        try:
            location = pyautogui.locateOnScreen(image_path, confidence=confidence)
            if location is not None:
                return location
            time.sleep(delay)
        except Exception as e:
            print(f"Waiting for image : {e}")
            time.sleep(delay)

def click_image(image_location):
    pyautogui.click(image_location)
    print(f"Image clicked : {image_location}")
