import relay_lib_seeed
import time

relay_lib_seeed.relay_on(4)
time.sleep(1)
relay_lib_seeed.relay_off(4)