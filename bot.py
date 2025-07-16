import pyautogui
import time
import random
from pynput import keyboard

# Five monster click locations
monster_clicks = [
    (940, 519),
    (1021, 562),
    (1122, 602),
    (1191, 576),
    (1263, 544)
]
occasional_x = 150
occasional_y = 430
next_level_x = 1174
next_level_y = 128
interval = 0.01
occasional_chance = 0.05

clicking = False
running = True
monster_index = 0

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
            # Rotate through monster click locations
            x, y = monster_clicks[monster_index]
            pyautogui.click(x, y)
            print(f"Clicked monster at ({x}, {y})")
            monster_index = (monster_index + 1) % len(monster_clicks)
            time.sleep(interval)

            if random.random() < occasional_chance:
                clicks = random.randint(1, 3)
                for _ in range(clicks):
                    pyautogui.click(occasional_x, occasional_y)
                    print(f"Clicked occasional at ({occasional_x}, {occasional_y})")
                    time.sleep(0.05)

            if random.random() < occasional_chance:
                clicks = random.randint(1, 3)
                for _ in range(clicks):
                    pyautogui.click(next_level_x, next_level_y)
                    print(f"Clicked next level at ({next_level_x}, {next_level_y})")
                    time.sleep(0.05)
        else:
            time.sleep(0.1)
except KeyboardInterrupt:
    print("\nStopped by user.")
