from urllib.request import urlopen
import time
import datetime
import winsound
import serial

frequency = 2500  # Set Frequency To 2500 Hertz
duration = 1000  # Set Duration To 1000 ms == 1 second

# ser = serial.Serial('COM5', baudrate=9600, timeout=1)
# time.sleep(3)

while True:
    try:
        urlopen('https://www.google.com')
        print("Connection found!", datetime.datetime.now())
        # ser.write(b'y')
    except:
        print("No connection found!", datetime.datetime.now())
        winsound.Beep(frequency, duration)
