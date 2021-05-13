import time
import paho.mqtt.client as mqtt
from . import relay_lib_seeed

mqtt_broker_ip = "localhost"
mqtt_channel = "quantum_cryptography/classical_channel"
client = mqtt.Client()

DELAY = 1  # in seconds.
RELAY = 1


def connect():
    client.connect(mqtt_broker_ip, 1883, 60)


def hello():
    print("pew pew pew!")


def trigger():
    relay_lib_seeed.relay_on(RELAY)
    client.publish(mqtt_channel, payload="laser/on", qos=0, retain=False)
    time.sleep(DELAY)
    client.publish(mqtt_channel, payload="laser/off", qos=0, retain=False)
    relay_lib_seeed.relay_off(RELAY)
