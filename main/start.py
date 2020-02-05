from machine import Pin
from time import sleep
import machine
import sys
import utime


# Pin definitions
repl_button = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP)
led = Pin(2, Pin.OUT)


    # If button 0 is pressed, drop to REPL
if repl_button.value() == 0:
    print("Dropping to REPL")
    sys.exit()

led.value(not led.value())
sleep(0.5)