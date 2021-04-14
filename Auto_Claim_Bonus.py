import pyautogui
import time
import winsound
frequency = 2500  # Set Frequency To 2500 Hertz
duration = 1  # Set Duration To 1000 ms == 1 second

while True:
    time.sleep(5)
    bonus_location = pyautogui.locateOnScreen('Click_to_claim_a_bonus.png', confidence=0.9)
    if bonus_location:
        print("bonus_location")
        print(bonus_location)
        print()
        bonus_point = pyautogui.center(bonus_location)
        bonus_x, bonus_y = bonus_point
        pyautogui.click(bonus_x, bonus_y)
        time.sleep(0.1)
        pyautogui.click(bonus_x, bonus_y)

    browser_error_detected = False
    if pyautogui.locateOnScreen('your_browser_encountered_an_error.PNG', confidence=0.9):
        browser_error_detected = True
    if pyautogui.locateOnScreen('your_browser_encountered_an_error_2.PNG', confidence=0.9):
        browser_error_detected = True
    if pyautogui.locateOnScreen('there_was_a_network_error.PNG', confidence=0.9):
        browser_error_detected = True
    if pyautogui.locateOnScreen('there_was_a_network_error_2.PNG', confidence=0.9):
        browser_error_detected = True
    if pyautogui.locateOnScreen('play_twitch.PNG', confidence=0.9):
        browser_error_detected = True
    if browser_error_detected:
        pyautogui.press('m')
        pyautogui.press('f5')
        time.sleep(30)
        pyautogui.press('m')
