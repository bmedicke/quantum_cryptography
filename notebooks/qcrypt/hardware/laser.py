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
    client.publish(laser_channel, payload="on", qos=0, retain=False)
    relay_lib_seeed.relay_on(RELAY)
    logging.info("laser: on")

    time.sleep(DELAY)

    client.publish(laser_channel, payload="off", qos=0, retain=False)
    relay_lib_seeed.relay_off(RELAY)
    logging.info("laser: off")


logging.basicConfig(
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(filename="laser.log", mode="a"),
    ],
    format="%(asctime)s: %(levelname)s - %(message)s",
    level=logging.INFO,
)
logging.info("laser module: imported")


mqtt_broker_ip = "localhost"
laser_channel = "quantum_cryptography/classical_channel/alice/laser"
client = mqtt.Client()
client.on_connect = on_connect
client.on_disconnect = on_disconnect
