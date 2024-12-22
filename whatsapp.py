import pyautogui as pt
from time import sleep
import pyperclip
import random


def get_message():
    """Retrieve the message from WhatsApp."""
    position1 = pt.locateOnScreen("smiley.png", confidence=0.6)
    if position1:
        x, y = position1[0], position1[1]
        pt.moveTo(x, y, duration=1)
        pt.moveTo(x + 70, y - 40, duration=1)
        pt.tripleClick()
        pt.rightClick()
        pt.moveRel(12, 15)
        pt.click()
        whatsapp_message = pyperclip.paste()
        print("Message received:", whatsapp_message)
        return whatsapp_message
    else:
        print("Smiley image not found.")
        return ""
def post_response(message):
    """Post a response in WhatsApp."""
    position1 = pt.locateOnScreen("smiley.png", confidence=0.6)
    if position1:
        x, y = position1[0], position1[1]
        pt.moveTo(x + 200, y + 20, duration=0.5)
        pt.click()
        pt.typewrite(message, interval=0.01)
        pt.typewrite("\n", interval=0.01)


