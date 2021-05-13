import time
from . import relay_lib_seeed

DELAY = 1 # in seconds.
RELAY = 1

def hello():
    print('pew pew pew!')

def trigger():
    relay_lib_seeed.relay_on(RELAY)
    time.sleep(DELAY)
    relay_lib_seeed.relay_off(RELAY)
