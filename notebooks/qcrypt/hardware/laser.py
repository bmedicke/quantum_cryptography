import time
import logging
import paho.mqtt.client as mqtt
from . import relay_lib_seeed


name = None
relay = None
delay = None
laser_channel = None


def init(username="alice", relay_id=1, delay_in_seconds=1):
    global name
    global relay
    global delay
    global laser_channel
    name = username
    relay = relay_id
    delay = delay_in_seconds
    laser_channel = f"quantum_cryptography/classical_channel/{name}/laser"
    logging.info(f"relay: selected number {relay_id}")
    logging.info(f"delay between on and off: {delay_in_seconds}s")
    client.connect(mqtt_broker_ip, 1883, 60)
    client.loop_start()


def on_connect(client, userdata, flags, rc):
    global name
    logging.info(f"mqtt: {name} connected")


def on_disconnect(client, userdata, rc):
    global name
    logging.warning(f"mqtt: {name} disconnected")


def trigger():
    global delay
    client.publish(laser_channel, payload="on", qos=0, retain=False)
    relay_lib_seeed.relay_on(relay)
    logging.info(f"laser relay {relay}: on")

    time.sleep(delay)

    client.publish(laser_channel, payload="off", qos=0, retain=False)
    relay_lib_seeed.relay_off(relay)
    logging.info(f"laser relay {relay}: off")


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
client = mqtt.Client()
client.on_connect = on_connect
client.on_disconnect = on_disconnect
