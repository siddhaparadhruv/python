import pyautogui


def take_screenshot():
    try:
        # Capture the screenshot of the entire screen
        screenshot = pyautogui.screenshot()

        # Save the screenshot to a file
        screenshot.save("screenshot.png")
        print("Screenshot saved successfully as 'screenshot.png'")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    take_screenshot()
