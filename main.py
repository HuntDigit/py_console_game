import os
import time
import threading

from datetime import datetime

width = 270 #80
height = 72 #24

offset1 = int(width // 2) - 1
offset2 = int(width // 2) - 1

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
        for i in range(0, height - 1):
            print("\033[{0};0H".format(str(i)) + lineUp)
        frame_pear_second = frame_pear_second + 1
        time.sleep(0.015)
        after_time = datetime.now()

        if datetime.timestamp(after_time) - datetime.timestamp(before_time) >= 1.0:
            print("\033[{0};2H{1} Press any key to stop programm".format(str(height), str(frame_pear_second)) + lineDown)
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
