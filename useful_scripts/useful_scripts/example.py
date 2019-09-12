"""
A simple example of hooking the keyboard on Linux using pyxhook

Any key pressed prints out the keys values, program terminates when spacebar
is pressed.
"""
from __future__ import print_function

# Libraries we need
import pyxhook
import time


import sys, termios, tty, os, time
import autopy

import os, os.path

try :
    os.makedirs('nude')
except FileExistsError as e :
    pass

try :
    os.makedirs('semi_nude')
except FileExistsError as e :
    pass

try :
    os.makedirs('animated')
except FileExistsError as e :
    pass

try :
    os.makedirs('porn')
except FileExistsError as e :
    pass

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
 
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch
 
button_delay = 0.2


DIR = 'porn'
n_porn = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])

DIR = 'semi_nude'
n_semi_nude = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])

DIR = 'nude'
n_nude = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])

DIR = 'animated'
n_animated = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])

print(n_nude , n_semi_nude , n_porn , n_animated)





"""
while True:
    char = getch()
 
    if (char == "p"):
        print("Stop!")
        exit(0)
 
    if (char == "a"):
        print("Left pressed")
        n_nude += 1
        bmp = autopy.bitmap.capture_screen()
        bmp.save('nude/nude{}.png'.format(n_nude))
        time.sleep(button_delay)
 
    elif (char == "d"):
        print("Right pressed")
        n_semi_nude += 1
        bmp = autopy.bitmap.capture_screen()
        bmp.save('semi_nude/semi_nude{}.png'.format(n_semi_nude))
        time.sleep(button_delay)
 
    elif (char == "w"):
        print("Up pressed")
        n_animated += 1
        bmp = autopy.bitmap.capture_screen()
        bmp.save('animated/animated{}.png'.format(n_animated))
        time.sleep(button_delay)
 
    elif (char == "s"):
        print("Down pressed")
        n_porn += 1
        bmp = autopy.bitmap.capture_screen()
        bmp.save('porn/porn{}.png'.format(n_porn))
        time.sleep(button_delay)
 
    elif (char == "1"):
        print("Number 1 pressed")
        time.sleep(button_delay)
"""



# This function is called every time a key is presssed
def kbevent(event):
    global running
    global n_nude
    global n_semi_nude
    global n_animated
    global n_porn
    global button_delay
    # print key info
    #print(event)

    # If the ascii value matches spacebar, terminate the while loop
    if event.Ascii == 113:
        running = False
        print('quitting')
    elif event.Ascii == 110:
        print("Left pressed")
        n_nude += 1
        bmp = autopy.bitmap.capture_screen()
        bmp.save('nude/nude{}.png'.format(n_nude))
        time.sleep(button_delay)
    elif event.Ascii == 115:
        print("Right pressed")
        n_semi_nude += 1
        bmp = autopy.bitmap.capture_screen()
        bmp.save('semi_nude/semi_nude{}.png'.format(n_semi_nude))
        time.sleep(button_delay)
    elif event.Ascii == 112:
        print("up pressed")
        n_porn += 1
        bmp = autopy.bitmap.capture_screen()
        bmp.save('porn/porn{}.png'.format(n_porn))
        time.sleep(button_delay)
    elif event.Ascii == 97:
        print("down pressed")
        n_animated += 1
        bmp = autopy.bitmap.capture_screen()
        bmp.save('animated/animated{}.png'.format(n_animated))
        time.sleep(button_delay)
#Create hookmanager
hookman = pyxhook.HookManager()
# Define our callback to fire when a key is pressed down
hookman.KeyDown = kbevent
# Hook the keyboard
hookman.HookKeyboard()
# Start our listener
hookman.start()

# Create a loop to keep the application running
running = True

button_delay = 0.2


DIR = 'porn'
n_porn = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])

DIR = 'semi_nude'
n_semi_nude = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])

DIR = 'nude'
n_nude = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])

DIR = 'animated'
n_animated = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])

#print(n_nude , n_semi_nude , n_porn , n_animated)

while running:
    time.sleep(0.1)

# Close the listener when we are done
hookman.cancel()
