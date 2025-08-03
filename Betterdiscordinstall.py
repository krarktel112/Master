    import pyautogui
    import time

    # Move to absolute coordinates (100, 200) instantly
    pyautogui.moveTo(100, 200)
    time.sleep(1) # Pause for 1 second

    # Move to (500, 500) over 2 seconds
    pyautogui.moveTo(500, 500, duration=2)
