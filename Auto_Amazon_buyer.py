import pyautogui
import time
import winsound
frequency = 2500  # Set Frequency To 2500 Hertz
duration = 1000  # Set Duration To 1000 ms == 1 second

# im2 = pyautogui.screenshot('my_screenshot.png')
print("Open and click on the Amazon product page of interest")
time.sleep(5)
print("Starting loop...")
while True:
    time.sleep(5)
    pyautogui.press('f5')
    time.sleep(5)
    pyautogui.press('home')
    time.sleep(5)
    buy_now_button_location = pyautogui.locateOnScreen('Buy_Now_2.png', confidence=0.9)
    if buy_now_button_location:
        print("buy_now_button_location")
        print(buy_now_button_location)
        print()
        buy_now_button_point = pyautogui.center(buy_now_button_location)
        buy_now_button_x, buy_now_button_y = buy_now_button_point
        pyautogui.click(buy_now_button_x, buy_now_button_y)
        winsound.Beep(frequency, duration)

        time.sleep(5)

    place_your_order_button_location = pyautogui.locateOnScreen('Place_your_order_2.png', confidence=0.9, grayscale=True)
    if place_your_order_button_location:
        print("place_your_order_button_location")
        print(place_your_order_button_location)
        print()
        place_your_order_button_point = pyautogui.center(place_your_order_button_location)
        place_your_order_button_x, place_your_order_button_y = place_your_order_button_point
        pyautogui.click(place_your_order_button_x, place_your_order_button_y)
        winsound.Beep(frequency, duration)

        time.sleep(5)

    green_check_location = pyautogui.locateOnScreen('green_check.png', confidence=0.9)
    if green_check_location:
        print("Order Placed!")
        winsound.Beep(frequency, duration)
        break
