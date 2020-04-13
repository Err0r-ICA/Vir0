#!/usr/bin/env python

import sys
import time

def delay(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)

delay
delay ("\033[48;5;0;38;5;197m Please, Enter Correct Number!")
print
delay ("\033[48;5;0;38;5;197m Now, Try Again...")
delay
