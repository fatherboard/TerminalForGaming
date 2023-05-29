import RPi.GPIO as GPIO
from subprocess import call, run
import time
import os

up = 11
down = 13

GPIO.setmode(GPIO.BOARD)
GPIO.setup(up,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(down,GPIO.IN, pull_up_down=GPIO.PUD_UP)


def buttonStateChanged(pin):
    mute = False
    while True:
        if not GPIO.input(up) | GPIO.input(down):
            if mute == False:
                call(["xdotool", "key", "XF86AudioMute"], shell=False)
                time.sleep(0.2)
                mute = True
                
            if mute == True:
                call(["xdotool", "key", "XF86AudioMute"], shell=False)
                time.sleep(0.2)
                mute = True
                
        if not GPIO.input(up):
            call(["xdotool", "key", "XF86AudioRaiseVolume"], shell=False)
            time.sleep(0.2)        
        if not GPIO.input(down):
            call(["xdotool", "key", "XF86AudioLowerVolume"], shell=False)
            time.sleep(0.2)
            
GPIO.add_event_detect(11, GPIO.BOTH, callback=buttonStateChanged)
GPIO.add_event_detect(13, GPIO.BOTH, callback=buttonStateChanged)

while True:
    time.sleep(5)    
