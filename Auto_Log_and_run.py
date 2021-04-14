import pyautogui
import time
import winsound
frequency = 2500  # Set Frequency To 2500 Hertz
duration = 10000  # Set Duration To 1000 ms == 1 second

done = False
while not done:
    time.sleep(10)
    start_button_location = pyautogui.locateOnScreen('Start_script.PNG', confidence=0.9)
    if start_button_location:
        print("start_button_location")
        print(start_button_location)
        print()
        start_button_point = pyautogui.center(start_button_location)
        start_button_x, start_button_y = start_button_point
        log_x_offset = 100
        log_y_offset = 100
        pyautogui.moveTo(start_button_x + log_x_offset, start_button_y + log_y_offset)
        pyautogui.click()
        pyautogui.keyDown('ctrl')
        pyautogui.press("a")
        pyautogui.keyUp('ctrl')
        pyautogui.keyDown('ctrl')
        pyautogui.press("c")
        pyautogui.keyUp('ctrl')

        log_notepad_location = pyautogui.locateOnScreen('log_notepad.PNG', confidence=0.9)
        log_notepad_point = pyautogui.center(log_notepad_location)
        log_notepad_x, log_notepad_y = log_notepad_point
        pyautogui.moveTo(log_notepad_x, log_notepad_y)
        pyautogui.click()
        pyautogui.keyDown('ctrl')
        pyautogui.press("v")
        pyautogui.keyUp('ctrl')
        pyautogui.keyDown('ctrl')
        pyautogui.press("s")
        pyautogui.keyUp('ctrl')

        # pyautogui.moveTo(start_button_x + log_x_offset, start_button_y + log_y_offset)
        # pyautogui.click()
        # pyautogui.moveTo(start_button_x, start_button_y)
        # pyautogui.click()

        done = True
        winsound.Beep(frequency, duration)
