#!/usr/bin/env python

import serial
import rtmidi

midiout = rtmidi.MidiOut()
available_ports = midiout.get_ports()

if available_ports:
    midiout.open_port(0)

ser = serial.Serial('/dev/tty.usbmodem1441', 31250)
while True:
    bytes = [ord(x) for x in ser.readline()[:-1]]
    if len(bytes) == 2:
        bytes.append(ord('\n'))
    if not bytes:
        continue
    print [hex(b) for b in bytes]
    midiout.send_message(bytes)
ser.close()
