import pyautogui
import time
import keyboard

# Replace 'phone_number' with the recipient's phone number
phone_number = ["7862902342", "7984654813", "Raj Paramhans"]

# Replace 'message_content' with the message you want to send
message_content = """
Hi, good afternoon. My name is Kishan and I am from Govardhan Institute. I hope you enjoyed our demo session of React, which is now over. Therefore, you will need to pay your fees in today's lecture. 
"""

# Open the WhatsApp APK
for i in phone_number:
    pyautogui.click(
        x=235, y=150
    )  # Replace coordinates with your WhatsApp app's location

    # Wait for the app to open
    pyautogui.write(i)
    time.sleep(3)

    pyautogui.click(
        x=210, y=218
    )  # Replace coordinates with your WhatsApp app's location

    # Wait for the chat to open
    time.sleep(3)

    # Split the message into lines and send each line separately
    lines = message_content.split("\n")

    pyautogui.hotkey("ctrl", "v")
    pyautogui.hotkey("enter")
    # pyautogui.hotkey('shift', 'enter')
    time.sleep(1)  # Adjust the sleep duration if needed

    # Wait for a moment before closing the application (optional)
    time.sleep(3)
    pyautogui.click(x=235, y=150)
    pyautogui.hotkey("ctrl", "a")
    pyautogui.hotkey("Back Space")
    # You can add additional code here to close the application or perform other actions if needed
