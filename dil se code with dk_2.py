
import pyautogui
import time
def message_sender(message):

    time.sleep(7)
    pyautogui.typewrite(message,interval=0.001)
    pyautogui.press("enter")
    print("message:",message)
message="plz man jao na"
message_sender(message)
