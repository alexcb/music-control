#!/usr/bin/python
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

# See https://pinout.xyz/ for pinouts

# The following pins have a physical pull up resistor
# we can't configure it via software, but in our case
# we want a pull up resistor anyway as the rotary switch
# will be connected to ground when the switch is closed
GPIO.setup(2, GPIO.IN)
GPIO.setup(3, GPIO.IN)


last_state = None
count = 0
dedent = None
last_dedent = None
while True:
    #gpio2, gpio3 = read_samples([2, 3], 1)
    gpio2 = GPIO.input(2)
    gpio3 = GPIO.input(3)

    state = (gpio2 ^ gpio3) | gpio2 << 1

    if state == 2 and dedent == None:
        dedent = count % 4 
        last_dedent = count

    if last_state is None:
        last_state = state
        continue
    if state == last_state:
        continue

    delta = (last_state - state) % 4
    last_state = state

    if delta == 3:
        count += 1
    if delta == 1:
        count -= 1

    if state == 2:
        dedent_delta = last_dedent - count
        count = count % 4
        last_dedent = count
        if dedent_delta > 0:
            print 'counter clockwise'
        elif dedent_delta < 0:
            print 'clockwise'
