
from pynput.keyboard import Key, KeyCode, Listener, Controller
import keyboard  # using module keyboard
import time

toggle = False
just_toggled_off = False


toggle_on_keys  = ['=', '\\']
toggle_off_keys = ['w', 'a', 's', 'd']
#toggle_off_keys = ['w']


# Allow toggle_on keys to break/turn-off autorun
TOGGLE_ON_BREAK = True



def toggle_on():
    global toggle
    global just_toggled_off

    toggle = True
    just_toggled_off = False


def toggle_off():
    global toggle
    global just_toggled_off

    toggle = False
    just_toggled_off = True


def toggle_func():
    global toggle
    global just_toggled_off

    toggle = not toggle

    if(not toggle):
        just_toggled_off = True



def execute():
    global toggle
    global just_toggled_off

    if(toggle):
        keyboard.press('w')

    if(not toggle and just_toggled_off):
        just_toggled_off = False
        keyboard.release('w')




# Main loop
while True:





    try:  # used try so that if user pressed other than the given key error will not be shown

        for key in toggle_on_keys:
            if keyboard.is_pressed(key):
                #print("Toggle on pressed")

                if (TOGGLE_ON_BREAK):
                    toggle_func()

                else:
                    toggle_on()

                #Sleep to eliminate key bouncing
                time.sleep(.1)


        for key in toggle_off_keys:
            if keyboard.is_pressed(key) and toggle:
                #print("Toggle off pressed")

                toggle_off()

                #Sleep to eliminate key bouncing
                time.sleep(.1)


    except:
        break  # if user pressed a key other than the given key the loop will break

    execute()
    time.sleep(.01)

#End main loop
