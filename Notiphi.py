# # Declare Imports
# from espeak import espeak
# import RPi.GPIO as GPIO
# from time import sleep
import pandas
import pandas as pd
import requests
from datetime import datetime
#
# espeak.synth("James you have a notification")
#
# # Set board pin mode
# GPIO.setmode(GPIO.BOARD)
#
# # Declare Pins
# NOTIPHI_BULB = 15
# SWITCH_1 = 13
# SWITCH_2 = 37
# SWITCH_3 = 36
# ACCEPT_BULB = 22
# REJECT_BULB = 29
# REMIND_BULB = 31
#
# # Set Pin modes
# GPIO.setup(NOTIPHI_BULB, GPIO.OUT)
# GPIO.setup(ACCEPT_BULB, GPIO.OUT)
# GPIO.setup(REJECT_BULB, GPIO.OUT)
# GPIO.setup(REMIND_BULB, GPIO.OUT)
# GPIO.setup(SWITCH_1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# GPIO.setup(SWITCH_2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# GPIO.setup(SWITCH_3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#
# # Blink Red bulb
# GPIO.output(NOTIPHI_BULB, GPIO.HIGH)
# print("LED ON")
# sleep(1)
# GPIO.output(NOTIPHI_BULB, GPIO.LOW)
# print("LED OFF")
# print(GPIO.input(SWITCH_1))
#
# # TEST OTHER BULBS
# GPIO.output(REMIND_BULB, GPIO.HIGH)
# print("REMIND LED ON")
# sleep(1)
#
# GPIO.output(REJECT_BULB, GPIO.HIGH)
# print("REJECT LED ON")
# sleep(1)
#
# GPIO.output(ACCEPT_BULB, GPIO.HIGH)
# print("ACCEPT LED ON")
# sleep(1)
#
# GPIO.output(REMIND_BULB, GPIO.LOW)
# print("REMIND LED OFF")
# print(GPIO.input(SWITCH_1))
# sleep(1)
#
# GPIO.output(REJECT_BULB, GPIO.LOW)
# print("REJECT LED OFF")
# sleep(1)
#
# GPIO.output(ACCEPT_BULB, GPIO.LOW)
# print("ACCEPT LED OFF")
# sleep(1)
#
# # STEADY THE SWITCH BULBS
# GPIO.output(REMIND_BULB, GPIO.HIGH)
# print("REMIND LED ON")
#
# GPIO.output(REJECT_BULB, GPIO.HIGH)
# print("REJECT LED ON")
#
# GPIO.output(ACCEPT_BULB, GPIO.HIGH)
# print("ACCEPT LED ON")
#
# # Run forever
#
# try:
#     while True:
#         SWITCH_1_STATE = GPIO.input(SWITCH_1)
#         SWITCH_2_STATE = GPIO.input(SWITCH_2)
#         SWITCH_3_STATE = GPIO.input(SWITCH_3)
#
#         if SWITCH_1_STATE == 1:
#             print("Button 1 Pressed")
#             sleep(0.2)
#
#         elif SWITCH_2_STATE == 1:
#             print("Button 2 Pressed")
#             sleep(0.2)
#
#         elif SWITCH_3_STATE == 1:
#             print("Button 3 Pressed")
#             sleep(0.2)
#
#
#         else:
#             continue
#
#
# except:
#     print("Quiting and Cleaning Up GPIO Pins")
#     GPIO.cleanup()


def preprocess(datum):
    return 0


def fetch_data(source, source_type="file"):
    data = []
    if source_type == "api":
        data = requests.get(url=source)
        data = preprocess(data)
        return data
    elif source_type == "file":
        data = pandas.read_excel(source)

    return data


infinite = True
button_green = True
button_red = False
button_blue = False
while infinite:
    notification_list = fetch_data(source="./api/notification.xlsx")
    infinite = False
    if notification_list.empty:
        print("Empty")
        continue

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    notification_list['alert_time'] = pd.to_datetime(notification_list['alert_time'], format="%Y-%m-%d %H:%M:%S")
    print(now)
    due = notification_list.loc[notification_list['alert_time'] < now]

    if button_blue:
        print(notification_list)
        notification_list["alert_time"] = notification_list["alert_time"] + + pd.Timedelta(hours=1)
        print(notification_list)

    elif button_green:
        for index, row in due.iterrows():
            print(row['message'], row["alert_time"])











