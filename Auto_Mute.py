import pyautogui
import time
import winsound
frequency = 2500  # Set Frequency To 2500 Hertz
duration = 1  # Set Duration To 1000 ms == 1 second

while True:
    time.sleep(0.1)
    bonus_location = pyautogui.locateOnScreen('youre_watching.PNG', confidence=0.9)
    if bonus_location:
        winsound.Beep(frequency, duration)
        pyautogui.press("m")
        time.sleep(120)
        pyautogui.press("m")
        winsound.Beep(frequency, duration)