import RPi.GPIO as GPIO
from subprocess import call, run
from datetime import datetime
import time


# pushbutton connected to this GPIO pin, using pin 5 also has the benefit of
# waking / powering up Raspberry Pi when button is pressed

# if button pressed for at least this long then shut down. if less then reboot.
shutdownMinSeconds = 3

# button debounce time in seconds
debounceSeconds = 0.01


GPIO.setmode(GPIO.BOARD)
GPIO.setup(5,GPIO.IN, pull_up_down=GPIO.PUD_UP)

buttonPressedTime = None


def buttonStateChanged(pin):
    global buttonPressedTime

    if not (GPIO.input(pin)):
        # button is down
        if buttonPressedTime is None:
            buttonPressedTime = datetime.now()
    else:
        # button is up
        if buttonPressedTime is not None:
            elapsed = (datetime.now() - buttonPressedTime).total_seconds()
            buttonPressedTime = None
            if elapsed >= shutdownMinSeconds:
                # button pressed for more than specified time, shutdown
                call(['shutdown', '-h', 'now'], shell=False)
            elif elapsed >= debounceSeconds:
                # button pressed for a shorter time, reboot
#                 run('vcgencmd display_power 0 2', shell = True)
#                 time.sleep(1)
#                 run('vcgencmd display_power 1 2', shell = True)
                call(['shutdown', '-r', 'now'], shell=False)
                
GPIO.add_event_detect(5, GPIO.BOTH, callback=buttonStateChanged)

while True:
    time.sleep(5)
  