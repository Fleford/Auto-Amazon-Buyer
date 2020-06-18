import pyautogui
import time
import winsound
frequency = 2500  # Set Frequency To 2500 Hertz
duration = 1  # Set Duration To 1000 ms == 1 second

time.sleep(5)

while True:
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

        time.sleep(5)
