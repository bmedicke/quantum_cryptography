import time
import logging
import paho.mqtt.client as mqtt
from . import relay_lib_seeed

DELAY = 1  # in seconds.
RELAY = 1


def on_connect(client, userdata, flags, rc):
    logging.info("mqtt: connected")


def on_disconnect(client, userdata, rc):
    logging.warning("mqtt: disconnected")


def connect():
    client.connect(mqtt_broker_ip, 1883, 60)
    client.loop_start()


def hello():
    logging.warning("pew pew pew!")


def trigger():
    client.publish(mqtt_channel, payload="laser/on", qos=0, retain=False)
    relay_lib_seeed.relay_on(RELAY)
    logging.info("laser: on")

    time.sleep(DELAY)

    client.publish(mqtt_channel, payload="laser/off", qos=0, retain=False)
    relay_lib_seeed.relay_off(RELAY)
    logging.info("laser: off")


logging.basicConfig(
    filename="laser.log",
    filemode="w",
    format="%(asctime)s: %(levelname)s - %(message)s",
    level=logging.INFO,
)
logging.info("laser module: imported")


mqtt_broker_ip = "localhost"
mqtt_channel = "quantum_cryptography/classical_channel"
client = mqtt.Client()
client.on_connect = on_connect
client.on_disconnect = on_disconnect
