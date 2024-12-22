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


def process_response(message):
    """Generate a response based on the message content."""
    if "?" in message.lower():
        return "Interesting question, I'll talk to you about that later - Bot GHDB"
    elif "hi" in message.lower():
        return "Hey, a bit busy right now. Just drop a message, I'll talk to you later - Bot GHDB"
    elif "happy new year" in message.lower():
        return "Wishing you and your family a very Happy New Year! ✨ - Bot GHDB"
    elif "good morning" in message.lower():
        return "Good Morning! Have a great day!"
    elif "good night" in message.lower():
        return "Good Night! Sleep tight!"
    else:
        return "Hello! GHDB is currently unavailable. Please leave a message - Bot GHDB"

def check_for_new_messages():
    # Re-locate the smiley image to update the coordinates
    position = pt.locateOnScreen("smiley.png", confidence=0.6)
    if position is not None:
        x, y = position[0], position[1]
    else:
        print("Smiley icon not found!")
        return

    pt.moveTo(x + 50, y - 45, duration=0.5)

    while True:
        try:
            position = pt.locateOnScreen("circle.png", confidence=0.6)
            if position:
                print("New message detected at:", position)
                pt.moveTo(position)
                pt.moveRel(-100, 0)
                pt.click()
                processed_message = process_response(get_message())
                post_response(processed_message)
                sleep(10)
            else:
                print("No new messages.")
                sleep(10)
        except pyautogui.ImageNotFoundException:
            print("Image not found. Check circle.png or smiley.png.")
            sleep(10)
        except Exception as e:
            print(f"Unexpected error: {e}")
            sleep(10)




# Start the bot
sleep(3)  # Allow time to prepare the screen
check_for_new_messages()


