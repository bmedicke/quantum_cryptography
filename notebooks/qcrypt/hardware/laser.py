import time
from . import relay_lib_seeed

DELAY = 1 # in seconds.

def hello():
    print('pew pew pew!')

def trigger():
    relay_lib_seeed.relay_on(4)
    time.sleep(DELAY)
    relay_lib_seeed.relay_off(4)
