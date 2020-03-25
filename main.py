import os
import time
import threading

from datetime import datetime
offset1 = 39
offset2 = 39

move_value = 1

isRendering = True

def render():
    frame_pear_second = 0
    before_time = datetime.now()
    after_time = datetime.now()
    while isRendering:
        v1 = offset1
        v2 = offset2
        lineUp = "=" * v1 + " " * 2 + "=" * v2
        lineDown = " "
        for i in range(0, 24):
            print("\033[{0};0H".format(str(i)) + lineUp)
        frame_pear_second = frame_pear_second + 1
        time.sleep(0.015)
        after_time = datetime.now()

        if datetime.timestamp(after_time) - datetime.timestamp(before_time) >= 1.0:
            print("\033[25;2H{0} Press any key to stop programm".format(str(frame_pear_second)) + lineDown)
            frame_pear_second = 0
            before_time = datetime.now()


render_thread = threading.Thread(target=render)
render_thread.start()

def move():
    while isRendering:
        time.sleep(0.040)
        global offset1
        global offset2
        global move_value

        offset1 += move_value
        offset2 -= move_value
        if offset1 <= 0 or offset2 <= 0:
            move_value = move_value * -1


render_thread_add = threading.Thread(target=move)
render_thread_add.start()

def interrupt():
    global isRendering
    key = input()
    isRendering = False
    os.system('clear')


render_thread_interrupt = threading.Thread(target=interrupt)
render_thread_interrupt.start()
