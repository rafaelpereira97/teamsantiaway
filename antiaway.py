import pyautogui
import random
import time

# Function to check for mouse activity
def is_mouse_active():
    current_pos = pyautogui.position()
    time.sleep(60)  # Sleep briefly
    new_pos = pyautogui.position()
    return current_pos != new_pos

while True:
    # Check if the mouse is active
    if not is_mouse_active():
        # Get the screen width and height
        screen_width, screen_height = pyautogui.size()

        # Generate random coordinates within the screen boundaries
        x = random.randint(0, screen_width)
        y = random.randint(0, screen_height)

        # Move the mouse to the random coordinates
        pyautogui.moveTo(x, y, duration=0.5)

    # Wait for 3 seconds
    time.sleep(3)
