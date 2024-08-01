import subprocess
import keyboard
import time
import sys

def simulate_typing(text, delay=0.1):
    for char in text:
        keyboard.write(char)
        sys.stdout.flush()
        time.sleep(delay)

# Run the dir command and capture its output
dir_output = "ls -l"

# Simulate typing the captured output with a typing effect
while 1:
    simulate_typing(dir_output)
    keyboard.press_and_release('enter')
    sys.stdout.flush()
    time.sleep(2)
