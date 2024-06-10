import pyautogui

try:
    while True:
        x, y = pyautogui.position()
        print(f"Cursor position: x = {x}, y = {y}")
except KeyboardInterrupt:
    print("\nScript terminated by user.")
