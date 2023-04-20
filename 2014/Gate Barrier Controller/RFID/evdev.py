#!/usr/bin/python
from evdev import device,util

devices = [device.InputDevice(fn) for fn in util.list_devices()]
for dev in devices:
   print(dev.fn, dev.name, dev.phys)
