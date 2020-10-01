#!/usr/bin/env python

from time import sleep

def delay(s):
    for c in s:
        print(c, end='', flush=True)
        sleep(0.01)

delay
delay ("\033[48;5;0;38;5;197m Please, Enter Correct Number!")
print
delay ("\033[48;5;0;38;5;197m Now, Try Again...")
delay
