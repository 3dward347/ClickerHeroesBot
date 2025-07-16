import pyautogui
import time
import random
from pynput import keyboard

main_x = 1100
main_y = 450
occasional_x = 150
occasional_y = 430
interval = 0.1
occasional_chance = 0.1

clicking = False
running = True

print("Starting in 3 seconds... Press 'z' to toggle, 'esc' to exit.")
time.sleep(3)

def on_press(key):
    global clicking, running
    try:
        if key.char == 'z':
            clicking = not clicking
            print("Clicking ON" if clicking else "Clicking OFF")
    except AttributeError:
        if key == keyboard.Key.esc:
            running = False
            print("Exiting...")
            return False

listener = keyboard.Listener(on_press=on_press)
listener.start()


try:
    while running:
        if clicking:
            pyautogui.click(main_x, main_y)
            print(f"Clicked main at ({main_x}, {main_y})")
            time.sleep(interval)

            if random.random() < occasional_chance:
                clicks = random.randint(1, 3)
                for _ in range(clicks):
                    pyautogui.click(occasional_x, occasional_y)
                    print(f"Clicked occasional at ({occasional_x}, {occasional_y})")
                    time.sleep(0.2)
        else:
            time.sleep(0.1)
except KeyboardInterrupt:
    print("\nStopped by user.")
