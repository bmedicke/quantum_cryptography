import time
import logging
from collections import defaultdict
import paho.mqtt.client as mqtt
from . import relay_lib_seeed

config = defaultdict(lambda: none)

def init(username="alice", relay_id=1, delay_in_seconds=1):
    global config
    config["name"] = username
    config["relay"] = relay_id
    config["delay"] = delay_in_seconds
    config[
        "laser_channel"
    ] = f"quantum_cryptography/classical_channel/{username}/laser"
    logging.info(f"relay: selected number {relay_id}")
    logging.info(f"delay between on and off: {delay_in_seconds}s")
    client.connect(mqtt_broker_ip, 1883, 60)
    client.loop_start()


def on_connect(client, userdata, flags, rc):
    global config
    logging.info(f"mqtt: {config['name']} connected")


def on_disconnect(client, userdata, rc):
    global config
    logging.warning(f"mqtt: {config['name']} disconnected")


def trigger():
    global config
    client.publish(config["laser_channel"], payload="on", qos=0, retain=False)
    relay_lib_seeed.relay_on(config["relay"])
    logging.info(f"laser relay {config['relay']}: on")

    time.sleep(config["delay"])

    client.publish(config["laser_channel"], payload="off", qos=0, retain=False)
    relay_lib_seeed.relay_off(config["relay"])
    logging.info(f"laser relay {config['relay']}: off")


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
