#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import subprocess
import time
from itertools import cycle

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

radio = {
    'kexp': 'http://216.246.37.218:80',
    'witr': 'http://streaming.witr.rit.edu:8000/witr-undrgnd-mp3-192.m3u',
#    'dfm':  'http://176.9.138.206:8205/dfm_1',
    'kcrw': 'http://newmedia.kcrw.com/legacy/pls/kcrwmusic.pls',
#    'irish': 'http://www.irishpubradio.com/streams1/listen.pls',
    }

radio_iter = cycle(radio.values())

state = None

next_try_is_playing = 0
def is_playing():
    try:
        x = subprocess.check_output(['/usr/bin/mpc', 'current']).strip()
    except Exception as e:
        return False
    return bool(x)

def set_volume():
    subprocess.call(['/usr/bin/mpc', 'volume', '100'])

def start_playing():
    if is_playing():
        return
    url = radio_iter.next()
    subprocess.call(['/usr/bin/mpc', 'clear'])
    subprocess.call(['/usr/bin/mpc', 'add', url])
    subprocess.call(['/usr/bin/mpc', 'play'])

def stop_playing():
    subprocess.call(['/usr/bin/mpc', 'stop'])

while True:
    input_state = GPIO.input(18)
    switched_on = input_state == False
    if switched_on:
        if state == None or state == 'off':
            start_playing()
            state = 'on'
    else:
        if state == None or state == 'on':
            stop_playing()
            state = 'off'
    if next_try_is_playing < time.time():
        next_try_is_playing = time.time() + 30
        set_volume()
        if not is_playing():
            state = None

