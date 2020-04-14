
import time
import sys
# Set color
R = '\033[1;91m' # Red
W = '\033[1;97m' # White
G = '\033[1;92m' # Green
O = '\033[1;93m' # Orange
B = '\033[1;94m' # Blue
M = '\033[1;95m' # magenta
C = '\033[1;96m' # cyan

def delay(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)
delay
delay (""+G+"  RR8RR                                  \n")
delay (""+G+"    8   eeee eeeee  eeeeeee e   e e    e \n")
delay (""+G+"    8e  8    8   8  8  8  8 8   8 8    8 \n")
delay (""+G+"    88  8eee 8eee8e 8e 8  8 8e  8 eeeeee \n")
delay (""+G+"    88  88   88   8 88 8  8 88  8 88   8 \n")
delay (""+G+"    88  88ee 88   8 88 8  8 88ee8 88   8 \n")
print
delay (""+W+" 8RRRR8                                 \n")
delay (""+W+" 8    8 eeee eeeee eeeee e   e    e     \n")
delay (""+W+" 8e   8 8    8   8 8   8 8   8    8     \n")
delay (""+W+" 88   8 8eee 8eee8 8e  8 8e  8eeee8     \n")
delay (""+W+" 88   8 88   88  8 88  8 88    88       \n")
delay (""+W+" 88eee8 88ee 88  8 88ee8 88eee 88       \n")
print
delay (""+R+"    88   8 *                               \n")
delay (""+R+"    88   8 e  eeeee  e   e eeeee           \n")
delay (""+R+"    88  e8 8  8   8  8   8 8   0           \n")
delay (""+R+"     8  8  8e 8eee8e 8e  8 8eeee           \n")
delay (""+R+"     8  8  88 88   8 88  8    88           \n")
delay (""+R+"     8ee8  88 88   8 88ee8 8ee88           \n")
print
