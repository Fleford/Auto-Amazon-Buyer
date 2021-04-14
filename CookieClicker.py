import pyautogui
import time
import cv2
import numpy as np
import matplotlib.pyplot as plt

# # Click on matching PNG
# start_button_location = pyautogui.locateOnScreen('Start_script.PNG', confidence=0.9)
# start_button_point = pyautogui.center(start_button_location)
# start_button_x, start_button_y = start_button_point
# pyautogui.moveTo(start_button_x, start_button_y)

# time.sleep(100)
# while True:
#     screenshot_mask = cv2.imread("screenshot_mask.png", 0)
#     pyautogui.moveTo(820, 160)
#     pyautogui.screenshot("screenshot.png")
#     screenshot_file_1 = cv2.imread("screenshot.png", 0)
#     time.sleep(1)
#     pyautogui.moveTo(820, 160)
#     pyautogui.screenshot("screenshot.png")
#     screenshot_file_2 = cv2.imread("screenshot.png", 0)
#     diff = cv2.subtract(screenshot_file_2, screenshot_file_1)
#     masked_diff = cv2.bitwise_and(diff, screenshot_mask, mask=None)
#
#     ret, thresh = cv2.threshold(masked_diff, 127, 255, 0)
#     M = cv2.moments(thresh)
#
#     if M["m00"]:
#         cX = int(M["m10"] / M["m00"])
#         cY = int(M["m01"] / M["m00"])
#         pyautogui.moveTo(cX, cY)
#         pyautogui.click()
#         print(cX, cY)
#         break

base_x = 820
base_y = 260
delta_y = 32
n_delta = 18

tlx = 220
delta_tlx = 560
tly = 220
delta_tly = 800


# pyautogui.moveTo(tlx + delta_tlx, tly + delta_tly)
# for x_coord in range(tlx, tlx + delta_tlx, 50):
#     for y_coord in range(tly, tly + delta_tly, 50):
#         pyautogui.moveTo(x_coord, y_coord)
#         pyautogui.click()


def FindGoldenCookie():
        pyautogui.moveTo(820, 160)
        pyautogui.screenshot("screenshot.png")
        screenshot_file_2 = cv2.imread("screenshot.png", 0)
        screenshot_file_1 = cv2.imread("screenshot_background.png", 0)
        screenshot_mask = cv2.imread("screenshot_mask.png", 0)
        diff = cv2.absdiff(screenshot_file_2, screenshot_file_1)
        masked_diff = cv2.bitwise_and(diff, screenshot_mask, mask=None)

        ret, thresh = cv2.threshold(masked_diff, 127, 255, 0)
        M = cv2.moments(thresh)

        if M["m00"]:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            pyautogui.moveTo(cX, cY)
            pyautogui.click()
            print(cX, cY)

            pyautogui.moveTo(820, 160)
            pyautogui.screenshot("screenshot_background.png")


pyautogui.moveTo(820, 160)
pyautogui.screenshot("screenshot_background.png")

while True:
    if n_delta == 0:
        n_delta = 18

        pyautogui.moveTo(820, 160)
        pyautogui.screenshot("screenshot_background.png")
        FindGoldenCookie()

        # Click on an upgrade
        pyautogui.moveTo(base_x, base_y - 50)
        pyautogui.click()

    n_delta -= 1
    pyautogui.moveTo(base_x, base_y + n_delta * delta_y)
    pyautogui.click()
    FindGoldenCookie()
