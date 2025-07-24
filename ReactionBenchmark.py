import pyautogui

while True:
    if pyautogui.pixel(286, 508) == (75, 219, 106):
        pyautogui.click()
        break