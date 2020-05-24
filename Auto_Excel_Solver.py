import pyautogui
import time
import winsound
frequency = 2500  # Set Frequency To 2500 Hertz
duration = 100  # Set Duration To 1000 ms == 1 second

time.sleep(5)

str_arry = ['$F$1', '$F$2', '$F$3', '$F$5', '$F$7']

for cell in str_arry:
    solver_button_location = pyautogui.locateOnScreen('Solver.png', confidence=0.9)
    if solver_button_location:
        print("solver_button_location")
        print(solver_button_location)
        print()
        solver_button_point = pyautogui.center(solver_button_location)
        solver_button_x, solver_button_y = solver_button_point
        pyautogui.click(solver_button_x, solver_button_y)
        winsound.Beep(frequency, duration)

    time.sleep(0.1)
    winsound.Beep(frequency, duration)
    pyautogui.press('tab')

    time.sleep(0.1)
    winsound.Beep(frequency, duration)
    pyautogui.press('tab')

    time.sleep(0.1)
    pyautogui.write(cell)
    winsound.Beep(frequency, duration)

    time.sleep(0.1)
    winsound.Beep(frequency, duration)
    pyautogui.press('tab')

    time.sleep(0.1)
    winsound.Beep(frequency, duration)
    pyautogui.press('tab')

    time.sleep(0.1)
    winsound.Beep(frequency, duration)
    pyautogui.press('s')

    Solver_Results_location = pyautogui.locateOnScreen('Solver_Results.PNG', confidence=0.9)
    while not Solver_Results_location:
        Solver_Results_location = pyautogui.locateOnScreen('Solver_Results.png', confidence=0.9)
    winsound.Beep(frequency, duration)
    pyautogui.press('enter')
