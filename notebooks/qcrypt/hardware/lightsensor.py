# standard libraries:
import time
import logging

# third party:
import paho.mqtt.client as mqtt

try:
    import RPi.GPIO as GPIO

    HARDWARE_IMPORTS = True
except ModuleNotFoundError as exception:
    print(f"{type(exception).__name__}: {exception}")
    HARDWARE_IMPORTS = False


class Lightsensor:
    pass
