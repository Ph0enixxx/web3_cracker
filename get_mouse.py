import pyautogui
import time

def display_mouse_position():
    last_pos = pyautogui.position()
    while True:
        new_pos = (pyautogui.position())
        if last_pos != new_pos:
            print(new_pos)
            last_pos = new_pos
        time.sleep(0.2)

if __name__ == '__main__':
    display_mouse_position()