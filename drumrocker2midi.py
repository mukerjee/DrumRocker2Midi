#!/usr/bin/env python

import threading
import time
import math
import pygame
import rtmidi

notes = {'snare': 38, 'high tom': 48,
         'mid tom': 47, 'floor tom': 43}

pygame.init()
pygame.joystick.init()
js = pygame.joystick.Joystick(0)
js.init()

midiout = rtmidi.MidiOut()
midiout.open_port(0)

last_vel = 0
last_time = 0


def play_note(note, vel):
    note_on = [0x99, note, vel]
    note_off = [0x99, note, 0]
    midiout.send_message(note_on)
    time.sleep(0.01)
    midiout.send_message(note_off)

print 'running...'
while 1:
    event = pygame.event.wait()
    # if js.get_button(7):  # drum
    note = 0
    if js.get_button(12):  # snare
        note = notes['snare']
        vel = js.get_axis(0)
    if js.get_button(14):  # high tom
        note = notes['high tom']
        vel = js.get_axis(1)
    if js.get_button(13):  # mid tom
        note = notes['mid tom']
        vel = js.get_axis(2)
    if js.get_button(11):  # floor tom
        note = notes['floor tom']
        vel = js.get_axis(3)
    if note:
        if vel == last_vel:
            continue
        t = time.time()
        # if (t - last_time) < 0.001:
        #     continue
        last_vel = vel
        last_time = t

        base = 10
        p = 127 / math.log(2, base)
        print p
        print vel
        vel = math.log((1 - vel) + 1.2, base)
        print vel
        vel = vel * p
        print vel
        print
        t = threading.Thread(target=play_note, args=(note, vel))
        t.start()
            
